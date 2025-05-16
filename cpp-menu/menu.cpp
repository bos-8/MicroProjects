/**
 * @file menu.cpp
 * @brief Console-based interactive menu.
 *
 * This utility implements a navigable console menu system with support
 * for keyboard navigation (arrows, hotkeys), color-coded text, and
 * cursor visibility management. Designed to integrate into larger
 * applications (e.g. raster rendering, toolchains).
 *
 * @author BO$ <https://github.com/bos-8>
 * @date 2025-05-11
 * @license GNU Affero General Public License v3.0 (AGPL-3.0)
 *
 * @details
 * Features:
 * - Highlighted selection with arrow or key shortcut.
 * - Customizable colors via MenuColor enum.
 * - Support for padding, visual cursor management.
 * - Modular structure suitable for embedding into other tools.
 */
#include <conio.h>
#include <windows.h>

#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

constexpr short padding_top = 0;
constexpr short padding_bottom = 0;
constexpr u_short MENU_INVALID_INDEX = 65535;

enum MenuColor {
    Default = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY,
    Highlight = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_INTENSITY,  // Yellow
    Selected = FOREGROUND_RED | FOREGROUND_BLUE | FOREGROUND_INTENSITY,    // Magenta
    KeyChar = FOREGROUND_BLUE | FOREGROUND_INTENSITY,                      // Light blue
    ValueText = FOREGROUND_GREEN | FOREGROUND_INTENSITY,                   // Light green
    DescriptionText = FOREGROUND_INTENSITY                                 // Grey
};

enum Key : int {
    Enter = 13,
    ArrowPrefix1 = 0,
    ArrowPrefix2 = 224,
    ArrowUp = 72,
    ArrowDown = 80,
    ArrowLeft = 75,
    ArrowRight = 77
};

struct Option {
    u_char Value[255];
    u_short Key;
    u_char Description[1024];
};

static HANDLE hConsole;

u_short menu(const std::vector<Option>& options);
void printWithColor(const char* text, MenuColor color);
void setCursorPosition(short x, short y);
short getCurrentCursorY();
void setCursorVisibility(bool visible);
u_short getMaxValueLength(const std::vector<Option>& options);
void drawMenuLine(const Option& opt, size_t maxLen, bool highlight);
void drawAllMenuLines(const std::vector<Option>& options, size_t maxLen, short baseY);
void handleUserInput(const std::vector<Option>& options, u_short& index, short baseY);
void drawSelectionMarker(short y, MenuColor color);

void printWithColor(const char* text, MenuColor color) {
    SetConsoleTextAttribute(hConsole, static_cast<WORD>(color));
    std::cout << text;
    SetConsoleTextAttribute(hConsole, static_cast<WORD>(MenuColor::Default));
}

void setCursorPosition(short x, short y) {
    COORD coord = {x, y};
    SetConsoleCursorPosition(hConsole, coord);
}

short getCurrentCursorY() {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(hConsole, &csbi);
    return csbi.dwCursorPosition.Y;
}

void setCursorVisibility(bool visible) {
    CONSOLE_CURSOR_INFO ci;
    GetConsoleCursorInfo(hConsole, &ci);
    if (static_cast<bool>(ci.bVisible) != visible) {
        ci.bVisible = visible ? TRUE : FALSE;
        SetConsoleCursorInfo(hConsole, &ci);
    }
}

u_short getMaxValueLength(const std::vector<Option>& options) {
    size_t maxLen = 0;
    for (const auto& opt : options)
        maxLen = max(maxLen, strlen((char*)opt.Value));
    return maxLen;
}

void drawMenuLine(const Option& opt, size_t maxLen, bool highlight) {
    std::cout << (highlight ? "> " : "  ");
    const char* val = (char*)opt.Value;

    for (size_t i = 0; val[i] != '\0'; ++i) {
        MenuColor color = (i == opt.Key) ? MenuColor::KeyChar : MenuColor::ValueText;
        printWithColor(std::string(1, val[i]).c_str(), color);
    }

    std::cout << std::setw((int)(maxLen - strlen(val) + 2)) << "  ";
    printWithColor((char*)opt.Description, MenuColor::DescriptionText);
    std::cout << "\n";
}

void drawAllMenuLines(const std::vector<Option>& options, size_t maxLen, short baseY) {
    for (size_t i = 0; i < options.size(); ++i) {
        setCursorPosition(0, baseY + i);
        drawMenuLine(options[i], maxLen, false);
    }
}

void handleUserInput(const std::vector<Option>& options, u_short& index, short baseY) {
    while (true) {
        int ch = _getch();

        if (ch == Key::ArrowPrefix1 || ch == Key::ArrowPrefix2) {
            int key = _getch();

            setCursorPosition(0, baseY + index);
            std::cout << "  ";

            if ((key == Key::ArrowUp || key == Key::ArrowLeft) && index > 0) {
                --index;
            } else if ((key == Key::ArrowDown || key == Key::ArrowRight) && index < options.size() - 1) {
                ++index;
            }

            drawSelectionMarker(baseY + index, MenuColor::Highlight);
        } else {
            ch = std::tolower(ch);

            for (size_t i = 0; i < options.size(); ++i) {
                char keyChar = std::tolower(options[i].Value[options[i].Key]);

                if (ch == keyChar) {
                    setCursorPosition(0, baseY + index);
                    std::cout << "  ";

                    index = static_cast<u_short>(i);
                    drawSelectionMarker(baseY + index, MenuColor::Highlight);
                    break;
                }
            }

            if (ch == Key::Enter)
                break;
        }
    }
}

void drawSelectionMarker(short y, MenuColor color) {
    setCursorPosition(0, y);
    printWithColor(">", color);
}

short getConsoleHeight() {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(hConsole, &csbi);
    return csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
}

/**
 * @brief Displays an interactive menu and returns selected option index.
 *
 * This function renders all menu entries with optional highlighted characters.
 * It supports navigation using arrow keys (↑↓←→) or a defined character shortcut.
 * Once the user confirms selection (Enter key), the selected index is returned.
 *
 * @param options A vector of Option structs containing the label, hotkey index, and description.
 * Example:
 * @code
 * std::vector<Option> options = {
 *     {"Option1", 0, "Description1"},
 *     {"Option2", 0, "Description2"}
 * };
 * u_short result = menu(options);
 * @endcode
 *
 * @return u_short Index of the selected option, or MENU_INVALID_INDEX if menu is empty or failed.
 *
 * @note The function hides the console cursor during interaction and restores it upon exit.
 * @warning Assumes console window and output encoding support for ASCII.
 */
u_short menu(const std::vector<Option>& options) {
    if (options.empty()) return MENU_INVALID_INDEX;
    hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    if (hConsole == INVALID_HANDLE_VALUE) return MENU_INVALID_INDEX;
    setCursorVisibility(false);
    u_short index = 0;
    size_t maxValLen = getMaxValueLength(options);
    drawAllMenuLines(options, maxValLen, getCurrentCursorY() + padding_top);
    short YMenuEnd = getCurrentCursorY();
    short YMenuStart = YMenuEnd - options.size();
    drawSelectionMarker(YMenuStart + index, MenuColor::Highlight);
    handleUserInput(options, index, YMenuStart);
    drawSelectionMarker(YMenuStart + index, MenuColor::Selected);
    std::cout << " ";
    printWithColor((char*)options[index].Value, MenuColor::Selected);
    setCursorPosition(0, YMenuEnd);
    for (short i = 0; i <= padding_bottom; ++i)
        std::cout << '\n';
    SetConsoleTextAttribute(hConsole, static_cast<WORD>(MenuColor::Default));
    setCursorVisibility(true);
    return index;
}
// EOF

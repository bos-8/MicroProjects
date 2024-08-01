# Author:       BO$ <https://github.com/bos-8>
# Description:  KeyDisplayer in PowerShell
# Date:         2024-07-23
# Version:      1.0
# Requirements: PowerShell 5.1, Windows 7/8/10/11

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$signature = @'
[DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)]
public static extern short GetAsyncKeyState(int virtualKeyCode);
'@

$API = Add-Type -MemberDefinition $signature -Name 'Keypress' -Namespace API -PassThru

$keysMap = @{
    0x01 = 'LMK'
    0x02 = 'PMK'
    0x04 = 'MMK'
    0x05 = 'X1MK'
    0x06 = 'X2MK'
    8    = 'BACKSPACE'
    9    = 'TAB'
    13   = 'ENTER'
    19   = 'PAUSE'
    20   = 'CAPS LOCK'
    27   = 'ESC'
    32   = 'SPACE'
    33   = 'PAGE UP'
    34   = 'PAGE DOWN'
    35   = 'END'
    36   = 'HOME'
    37   = 'LEFT ARROW'
    38   = 'UP ARROW'
    39   = 'RIGHT ARROW'
    40   = 'DOWN ARROW'
    45   = 'INSERT'
    46   = 'DELETE'
    48   = '0'
    49   = '1'
    50   = '2'
    51   = '3'
    52   = '4'
    53   = '5'
    54   = '6'
    55   = '7'
    56   = '8'
    57   = '9'
    65   = 'A'
    66   = 'B'
    67   = 'C'
    68   = 'D'
    69   = 'E'
    70   = 'F'
    71   = 'G'
    72   = 'H'
    73   = 'I'
    74   = 'J'
    75   = 'K'
    76   = 'L'
    77   = 'M'
    78   = 'N'
    79   = 'O'
    80   = 'P'
    81   = 'Q'
    82   = 'R'
    83   = 'S'
    84   = 'T'
    85   = 'U'
    86   = 'V'
    87   = 'W'
    88   = 'X'
    89   = 'Y'
    90   = 'Z'
    91   = 'LEFT WIN'
    92   = 'RIGHT WIN'
    93   = 'APPS'
    96   = 'NUMPAD 0'
    97   = 'NUMPAD 1'
    98   = 'NUMPAD 2'
    99   = 'NUMPAD 3'
    100  = 'NUMPAD 4'
    101  = 'NUMPAD 5'
    102  = 'NUMPAD 6'
    103  = 'NUMPAD 7'
    104  = 'NUMPAD 8'
    105  = 'NUMPAD 9'
    106  = 'NUMPAD *'
    107  = 'NUMPAD +'
    109  = 'NUMPAD -'
    110  = 'NUMPAD .'
    111  = 'NUMPAD /'
    112  = 'F1'
    113  = 'F2'
    114  = 'F3'
    115  = 'F4'
    116  = 'F5'
    117  = 'F6'
    118  = 'F7'
    119  = 'F8'
    120  = 'F9'
    121  = 'F10'
    122  = 'F11'
    123  = 'F12'
    144  = 'NUM LOCK'
    145  = 'SCROLL LOCK'
    186  = ';'
    187  = '='
    188  = ','
    189  = '-'
    190  = '.'
    191  = '/'
    192  = '`'
    219  = '['
    220  = '\'
    221  = ']'
    222  = '\'
}

$form = New-Object System.Windows.Forms.Form
$form.Text = "KEY DISPLAYER"
$form.Size = New-Object System.Drawing.Size(300, 80)
$form.BackColor = [System.Drawing.Color]::Black
$form.TopMost = $true

$button = New-Object System.Windows.Forms.Button
$button.Text = "KEY DISPLAYER"
$button.Font = New-Object System.Drawing.Font("Consolas", 30, [System.Drawing.FontStyle]::Bold)
$button.ForeColor = [System.Drawing.Color]::White
$button.BackColor = [System.Drawing.Color]::Black
$button.Dock = [System.Windows.Forms.DockStyle]::Fill
$button.TextAlign = [System.Drawing.ContentAlignment]::MiddleCenter

$script:btn_active = $false
$script:stopLoop = $false

$button.Add_Click({
        if ($script:btn_active) {
            $button.Text = "CLICKED"
            $script:btn_active = $false
            $script:stopLoop = $false
            $form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::None
            $form.Size = [System.Drawing.Size]::new(300, 50)
            Start-Key
        }
        else {
            $button.Text = "Start"
            $form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::Sizable
            $form.Size = [System.Drawing.Size]::new(300, 80)
            $script:btn_active = $true
            $script:stopLoop = $true
        }
        $form.Refresh()
    })

$form.Controls.Add($button)

# [void] $form.ShowDialog()
# $form.Show()

$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 50
function Start-Key {
    # Write-Host "Start-Key"
    $timer.Add_Tick({
            if ($script:stopLoop) {
                # Write-Host "Stop-Key"
                $timer.Stop()
                return
            }

            $commbo = ''
            $key = ''
            for ($ascii = 1; $ascii -le 255; $ascii++) {
                if (($ascii -eq 16) -or ($ascii -eq 17) -or ($ascii -eq 18) ) {
                    #-or ($ascii -eq 161) -or ($ascii -eq 162) -or ($ascii -eq 163)
                    continue
                }
                if ($API::GetAsyncKeyState($ascii) -lt 0) {
                    $key = [char]$ascii
                    if ($keysMap.ContainsKey($ascii)) {
                        $key = $keysMap[$ascii]
                    }
                    if ($key -eq 'NUM LOCK') {
                        $form.Close()
                        return
                    }
                    $shiftPressed = ($API::GetAsyncKeyState(16) -lt 0)
                    $ctrlPressed = ($API::GetAsyncKeyState(17) -lt 0)
                    $altPressed = ($API::GetAsyncKeyState(18) -lt 0)

                    if ($shiftPressed -and ($key -ne '')) {
                        $commbo += 'SHIFT + '
                    }
                    if ($ctrlPressed -and ($key -ne '')) {
                        $commbo += 'CTRL + '
                    }
                    if ($altPressed -and ($key -ne '')) {
                        $commbo += 'ALT + '
                    }
                    # Write-Host "KEY: $commbo$key"
                    $button.Text = $commbo + $key
                    $form.Refresh()
                    break
                }
            }
        })

    $timer.Start()
}
[void]$form.ShowDialog()
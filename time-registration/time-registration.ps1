<#
.SYNOPSIS
Measures time spent on a task and saves the data to CSV files in multiple locations.
.DESCRIPTION
This script allows users to track time spent on tasks by prompting them for task details (task name, client, and description).
It starts a timer when the task begins and stops the timer once the user finishes. The task details, along with the start time, end time, and total time spent, are saved into a CSV file. The CSV file is saved in two locations: the user's desktop directory, and the script's directory.
.EXAMPLE
# Running the script to track a task
.\TaskTimeTracker.ps1
.NOTES
Version:        0x001b
Date:           2024-10-04
Update:         2024-10-06
Author:         BO$ <https://github.com/bos-8>
Requirements:   PowerShell 5.1, Windows 10/11
.INPUTS
NONE
.OUTPUTS
NONE
.LINK
NONE
#>

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$filePath = "$PSScriptRoot\time-registration.csv"
$homeFilePath = "$env:USERPROFILE\Documents\time-registration.csv" # $HOME

$global:startTime = $null
$global:timerRunning = $false
$timer = New-Object System.Windows.Forms.Timer
# $timer.Interval = 1000  # 1-second interval
$timer.Interval = 60000  # 1-minute interval

# HIDE CONSOLE PROMPT
$consoleWindow = Get-Process -Id $PID
$consoleWindow.MainWindowHandle | ForEach-Object {
    $win32 = @"
        [DllImport("user32.dll")]
        public static extern bool ShowWindow(int hWnd, int nCmdShow);
"@
    $type = Add-Type -MemberDefinition $win32 -Name Win32ShowWindow -Namespace Win32Functions -PassThru
    $type::ShowWindow($_, 0)  # 0 = SW_HIDE
}

#region Functions
function Update-TimerLabel {
    $elapsedTime = (Get-Date) - $global:startTime
    # $formattedElapsedTime = "{0:00}:{1:00}:{2:00}" -f $elapsedTime.Hours, $elapsedTime.Minutes, $elapsedTime.Seconds
    $formattedElapsedTime = "{0:00}:{1:00}" -f $elapsedTime.Hours, $elapsedTime.Minutes
    $timerLabel.Text = $formattedElapsedTime
    $timerLabel.Refresh()
}

function checkFile ($file) {
    if (!(Test-Path -Path $file)) {
        "date;time;start_time;end_time;task;client;description;" | Out-File -FilePath $file -Encoding UTF8
    }
    saveDataToCSV ($file)
}

function saveDataToCSV($file) {
    $date = Get-Date -Format "yyyy-MM-dd"
    $endTime = Get-Date
    $time = $timerLabel.Text
    $task = $taskInput.Text
    $client = $customerInput.Text
    $description = $descriptionInput.Text
    $description = $description -replace "`r`n", "\n" -replace "`n", "\n"
    Write-Host "Saving data to $file"
    if (Test-Path -Path $file) {
        $lineToAdd = "$date;$time;$global:startTime;$endTime;$task;$client;$description;"
        Add-Content -Path $file -Value $lineToAdd -Encoding 'UTF8'
    }
    else {
        $errorMessage = "File $file not found"
        [System.Windows.Forms.MessageBox]::Show($errorMessage, "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    }
}

function OnFormClosed {
    Write-Host "ON CLOSE"
    if ($global:timerRunning) {
        $timer.Stop()
        $timer.Dispose()
        checkFile($filePath)
        checkFile($homeFilePath)
    }
    $form.Dispose()
}
#endregion

#region GUI
$form = New-Object System.Windows.Forms.Form
$form.Text = "TIME REGISTRATION"
$form.Size = New-Object System.Drawing.Size(400, 350)
$form.BackColor = [System.Drawing.ColorTranslator]::FromHtml("#222222")
$form.StartPosition = "CenterScreen"
$form.Font = New-Object System.Drawing.Font("Consolas", 10, [System.Drawing.FontStyle]::Bold)
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedDialog
$form.MaximizeBox = $false

# Timer Panel
$timerPanel = New-Object Windows.Forms.Panel
$timerPanel.Dock = [System.Windows.Forms.DockStyle]::Top
$timerPanel.Height = 50
$form.Controls.Add($timerPanel)

# Timer display
$timerLabel = New-Object Windows.Forms.Label
$timerLabel.Text = "00:00"
$timerLabel.Font = New-Object System.Drawing.Font("Consolas", 32, [System.Drawing.FontStyle]::Bold)
$timerLabel.ForeColor = [System.Drawing.Color]::White
$timerLabel.Dock = [System.Windows.Forms.DockStyle]::Fill
$timerLabel.TextAlign = [System.Drawing.ContentAlignment]::MiddleCenter
$timerPanel.Controls.Add($timerLabel)

# Task label
$taskLabel = New-Object Windows.Forms.Label
$taskLabel.Text = "TASK*:"
$taskLabel.ForeColor = [System.Drawing.Color]::White
$taskLabel.Location = New-Object System.Drawing.Point(10, 60)
$taskLabel.AutoSize = $true
$form.Controls.Add($taskLabel)

# Task input
$taskInput = New-Object Windows.Forms.TextBox
$taskInput.Location = New-Object System.Drawing.Point(10, 80)
$taskInput.Width = 360
$taskInput.BackColor = [System.Drawing.ColorTranslator]::FromHtml("#444444")
$taskInput.ForeColor = [System.Drawing.Color]::White
$taskInput.BorderStyle = [System.Windows.Forms.BorderStyle]::FixedSingle
$form.Controls.Add($taskInput)

# Customer label
$customerLabel = New-Object Windows.Forms.Label
$customerLabel.Text = "CUSTOMER*:"
$customerLabel.ForeColor = [System.Drawing.Color]::White
$customerLabel.Location = New-Object System.Drawing.Point(10, 110)
$customerLabel.AutoSize = $true
$form.Controls.Add($customerLabel)

# Customer input
$customerInput = New-Object Windows.Forms.TextBox
$customerInput.Location = New-Object System.Drawing.Point(10, 130)
$customerInput.Width = 360
$customerInput.BackColor = [System.Drawing.ColorTranslator]::FromHtml("#444444")
$customerInput.ForeColor = [System.Drawing.Color]::White
$customerInput.BorderStyle = [System.Windows.Forms.BorderStyle]::FixedSingle
$form.Controls.Add($customerInput)

# Description label
$descriptionLabel = New-Object Windows.Forms.Label
$descriptionLabel.Text = "DESCRIPTION:"
$descriptionLabel.ForeColor = [System.Drawing.Color]::White
$descriptionLabel.Location = New-Object System.Drawing.Point(10, 160)
$descriptionLabel.AutoSize = $true
$form.Controls.Add($descriptionLabel)

# Description input
$descriptionInput = New-Object Windows.Forms.TextBox
$descriptionInput.Multiline = $true
$descriptionInput.Location = New-Object Drawing.Point(10, 180)
$descriptionInput.Size = New-Object Drawing.Size(360, 60)
$descriptionInput.BackColor = [System.Drawing.ColorTranslator]::FromHtml("#444444")
$descriptionInput.ForeColor = [System.Drawing.Color]::White
$descriptionInput.BorderStyle = [System.Windows.Forms.BorderStyle]::FixedSingle
$form.Controls.Add($descriptionInput)

# Button Panel
$buttonPanel = New-Object Windows.Forms.Panel
$buttonPanel.Dock = [System.Windows.Forms.DockStyle]::Bottom
$buttonPanel.Height = 60
$form.Controls.Add($buttonPanel)

# Start Button
$startButton = New-Object Windows.Forms.Button
$startButton.Text = "START"
$startButton.BackColor = [System.Drawing.Color]::Green
$startButton.ForeColor = [System.Drawing.Color]::White
$startButton.Font = New-Object System.Drawing.Font("Consolas", 16, [System.Drawing.FontStyle]::Bold)
$startButton.Width = 100
$startButton.Height = 25
$startButton.Location = New-Object Drawing.Point(30, 10)
$buttonPanel.Controls.Add($startButton)

# Stop Button
$stopButton = New-Object Windows.Forms.Button
$stopButton.Text = "STOP"
$stopButton.BackColor = [System.Drawing.Color]::Red
$stopButton.ForeColor = [System.Drawing.Color]::White
$stopButton.Font = New-Object System.Drawing.Font("Consolas", 16, [System.Drawing.FontStyle]::Bold)
$stopButton.Width = 100
$stopButton.Height = 25
$stopButton.Location = New-Object Drawing.Point(240, 10)
$buttonPanel.Controls.Add($stopButton)

# Version Label
$versionLabel = New-Object Windows.Forms.Label
$versionLabel.Text = "v0x001b by BO$"
$versionLabel.ForeColor = [System.Drawing.Color]::Gray
$versionLabel.Font = New-Object System.Drawing.Font("Consolas", 10, [System.Drawing.FontStyle]::Regular)
$versionLabel.AutoSize = $true
$versionLabel.Location = New-Object System.Drawing.Point(265, 45)
$buttonPanel.Controls.Add($versionLabel)
#endregion

$startButton.Enabled = $false
$stopButton.Enabled = $false

$updateStartButton = {
    $startButton.Enabled = -not [string]::IsNullOrWhiteSpace($taskInput.Text) -and -not [string]::IsNullOrWhiteSpace($customerInput.Text)
}

$taskInput.Add_TextChanged($updateStartButton)
$customerInput.Add_TextChanged($updateStartButton)

$startButton.Add_Click({
        $startButton.Enabled = $false
        $stopButton.Enabled = $true
        $taskInput.Enabled = $false
        $customerInput.Enabled = $false
        $descriptionInput.Enabled = $false
        $timerLabel.Text = "00:00"
        $timerLabel.ForeColor = [System.Drawing.Color]::Green
        $timerLabel.Refresh()

        $global:timerRunning = $true
        $global:startTime = Get-Date
        $timer.Add_Tick({ Update-TimerLabel })
        $timer.Start()
    })

$stopButton.Add_Click({
        $timer.Stop()
        $stopButton.Enabled = $false
        $startButton.Enabled = $true
        $taskInput.Enabled = $true
        $customerInput.Enabled = $true
        $descriptionInput.Enabled = $true
        $timerLabel.ForeColor = [System.Drawing.Color]::White
        $timerLabel.Refresh()
        $timer.Stop()
        $timer.Dispose()

        $global:timerRunning = $false

        Write-Host "ON STOP"

        checkFile($filePath)
        checkFile($homeFilePath)
    })

$form.Add_FormClosed({
        OnFormClosed
    })

[void]$form.ShowDialog()
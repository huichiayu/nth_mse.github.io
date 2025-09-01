# Bash vs PowerShell Cheat Sheet

| Operation | Bash (Unix) | PowerShell | Description |
|-----------|-------------|------------|-------------|
| List files | `ls` | `Get-ChildItem` (`dir`, `ls`) | Show directory contents |
| Change directory | `cd` | `Set-Location` (`cd`) | Navigate directories |
| Copy files | `cp` | `Copy-Item` (`cp`) | Copy files or directories |
| Move files | `mv` | `Move-Item` (`mv`) | Move or rename files |
| Remove files | `rm` | `Remove-Item` (`rm`, `del`) | Delete files or directories |
| Create directory | `mkdir` | `New-Item -Type Directory` (`mkdir`) | Create new directory |
| Show file content | `cat` | `Get-Content` (`cat`, `type`) | Display file contents |
| Find text | `grep` | `Select-String` (`findstr`) | Search for text patterns |
| Current location | `pwd` | `Get-Location` (`pwd`) | Show current directory |
| Clear screen | `clear` | `Clear-Host` (`cls`) | Clear terminal screen |
| Compare files | `diff` | `Compare-Object` | Compare file contents |
| Process list | `ps` | `Get-Process` | List running processes |
| Kill process | `kill` | `Stop-Process` | Terminate process |
| Network info | `ifconfig` | `Get-NetIPConfiguration` | Show network configuration |
| Permission change | `chmod` | `Set-Acl` | Change file permissions |
| View file tail | `tail` | `Get-Content -Tail` | Show end of file |
| System info | `uname -a` | `Get-ComputerInfo` | Display system information |

Note: PowerShell commands in parentheses are aliases that make PowerShell feel more familiar to Bash users. PowerShell commands are not case-sensitive, while Bash commands are.

Common tips:
- PowerShell uses verb-noun naming convention (e.g., `Get-Process`)
- PowerShell aliases allow Unix-style commands to work
- PowerShell commands can output objects, while Bash outputs text streams
- Both shells support pipeline operations, but PowerShell pipes objects rather than text
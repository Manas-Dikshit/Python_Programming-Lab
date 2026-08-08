# Setting Up Git on Windows, macOS, and Linux

This guide walks through installing Git, configuring it, and verifying the installation on all three major operating systems.

---

## 1. Windows

### Option A: Installer (Recommended)
1. Download the latest installer from the [official Git website](https://git-scm.com/download/win).
2. Run the downloaded `.exe` file.
3. Follow the wizard; the default settings work fine for most users.
4. During setup, choose the default Git Bash terminal option.
5. Click **Finish** once installation is complete.

### Option B: Chocolatey (Package Manager)
```powershell
choco install git -y
```

### Option C: Winget (Built-in)
```powershell
winget install --id Git.Git -e --source winget
```

### Verify Installation
```powershell
git --version
```

---

## 2. macOS

### Option A: Homebrew (Recommended)
If Homebrew is not installed, install it first:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Git:

```bash
brew install git
```

### Option B: Xcode Command Line Tools
```bash
xcode-select --install
```

This installs Git as part of the command line tools. Confirm the license if prompted.

### Verify Installation
```bash
git --version
```

---

## 3. Linux (Debian/Ubuntu, Fedora, Arch)

### Debian / Ubuntu (apt)
```bash
sudo apt update
sudo apt install git -y
```

### Fedora / RHEL (dnf)
```bash
sudo dnf install git -y
```

### Arch Linux (pacman)
```bash
sudo pacman -S git
```

### Verify Installation
```bash
git --version
```

---

## 4. Post-Installation Configuration

Git needs your identity for commits. Run these commands after installation on any OS:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Optional: Set Default Editor
```bash
git config --global core.editor "code --wait"
```

### Verify Configuration
```bash
git config --list
```

---

## 5. Getting Started

Once Git is installed and configured, initialize a repository:

```bash
git init
```

Or clone an existing one:

```bash
git clone <repository-url>
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `git` is not recognized as a command | Re-open your terminal/PowerShell, or restart your computer after install |
| Permission denied while installing | Use `sudo` on Linux/macOS, or run the installer as Administrator on Windows |
| Old version installed | Update via your package manager or download the latest installer |

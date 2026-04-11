!include "MUI2.nsh"

!define MUI_ICON "..\design\logo_icon.ico"

Name "Vadim's Clicker"
InstallDir "$PROGRAMFILES\VadimsClicker"
OutFile "VadimsClicker.exe"
BrandingText "Liubomyr Pryt"


!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_DIRECTORY
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH


!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "Ukrainian"

!define DISTDIR "vadim-clicker.dist"

Function .onInit
    !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section ""
    

    SetOutPath $INSTDIR
    File /r /x tui.exe /x gui.exe ..\dist\${DISTDIR}
    
    CreateDirectory "$SMPROGRAMS\VadimsClicker"
    
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker" "DisplayName" "VadimsClicker"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker" "DisplayVersion" "0.1.0.0"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker" "Publisher" "Pryt Liubomyr"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker" "NoRepair" 1
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker" "UninstallString" "$INSTDIR\uninstall.exe"
SectionEnd


Section "TUI"
    SetOutPath $INSTDIR\${DISTDIR}
    File "..\dist\${DISTDIR}\tui.exe"
    
    SetOutPath $INSTDIR
    File vc.bat
    
    CreateShortCut "$SMPROGRAMS\VadimsClicker\vc.lnk" "$INSTDIR\${DISTDIR}\tui.exe"
    EnVar::AddValue "Path" "$INSTDIR"
SectionEnd

Section "GUI"
    SetOutPath $INSTDIR\${DISTDIR}
    File "..\dist\vadim-clicker.dist\gui.exe"
    
    CreateShortCut "$DESKTOP\VadimsClicker.lnk" "$INSTDIR\${DISTDIR}\gui.exe"
    CreateShortCut "$SMPROGRAMS\VadimsClicker\VadimsClicker.lnk" "$INSTDIR\${DISTDIR}\gui.exe"
    CreateShortCut "$SMPROGRAMS\VadimsClicker\vc.lnk" "$INSTDIR\${DISTDIR}\tui.exe"
SectionEnd


Section "Uninstall"
    RMDir /r "$INSTDIR"
    Delete "$DESKTOP\VadimsClicker.lnk"
    RMDir /r "$SMPROGRAMS\VadimsClicker"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VadimsClicker"
    EnVar::DeleteValue "Path" "$INSTDIR"
SectionEnd
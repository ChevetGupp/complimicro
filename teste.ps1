# Obter o caminho da pasta atual do script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

# Definir o caminho da pasta de instalação dos programas
$folderPath = Join-Path $scriptPath "apps/teste"

# Caminho para o instalador do aplicativo
$instalador = Join-Path $folderPath "MediaCreationTool22H2.exe"

# Verifique se o instalador existe
if (Test-Path $instalador) {
    # Execute o instalador silenciosamente
    Start-Process -FilePath $instalador -ArgumentList "/S" -Wait

    # Verifique se a instalação foi bem-sucedida
    if ($?) {
        Write-Host "Instalação concluída com sucesso."
    } else {
        Write-Host "A instalação falhou."
    }
} else {
    Write-Host "O instalador não foi encontrado em $instalador."
}

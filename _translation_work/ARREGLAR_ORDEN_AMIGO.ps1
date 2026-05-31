# Arregla el orden de carga de mods para que coincida con el del host.
# El amigo: cerrar el juego, clic derecho en este archivo -> "Ejecutar con PowerShell".
$ErrorActionPreference = "Stop"
$s = Get-ChildItem "$env:APPDATA\SlayTheSpire2\steam\*\settings.save" -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $s) { Write-Host "No encontre settings.save. Abri el juego al menos una vez." ; pause; exit }
Copy-Item $s.FullName "$($s.FullName).backup_sync" -Force
$j = Get-Content $s.FullName -Raw | ConvertFrom-Json
$top = @('BaseLib','ModConfig')
$sorted = $j.mod_settings.mod_list | Sort-Object `
  @{Expression={ if ($top -contains $_.id) {0} else {1} }}, `
  @{Expression={ $i = [array]::IndexOf($top, $_.id); if ($i -ge 0) { '{0:00}' -f $i } else { $_.id.ToLower() } }}
$j.mod_settings.mod_list = @($sorted)
$j | ConvertTo-Json -Depth 25 | Set-Content $s.FullName -Encoding utf8
Write-Host "Listo. Orden nuevo:" -ForegroundColor Green
$i=1; foreach ($m in $j.mod_settings.mod_list) { Write-Host ("  {0,2}. {1}" -f $i,$m.id); $i++ }
Write-Host "Respaldo en: $($s.FullName).backup_sync"
pause

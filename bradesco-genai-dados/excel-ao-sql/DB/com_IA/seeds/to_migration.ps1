# Script para automatizar a execução dos scripts da pasta seeds

# Define o caminho da pasta seeds
$seedsPath = ".\seeds"

# Verifica se a pasta seeds existe
if (-Not (Test-Path $seedsPath)) {
    Write-Host "Pasta 'seeds' não encontrada!" -ForegroundColor Red
    exit 1
}

# Obtém todos os arquivos .sql da pasta seeds e ordena por nome para execução sequencial
$sqlFiles = Get-ChildItem -Path $seedsPath -Filter "*.sql" | Sort-Object Name

if ($sqlFiles.Count -eq 0) {
    Write-Host "Nenhum arquivo .sql encontrado na pasta seeds!" -ForegroundColor Yellow
    exit 0
}

Write-Host "Executando scripts da pasta seeds em ordem alfabética..." -ForegroundColor Green
Write-Host "Ordem de execução:" -ForegroundColor Cyan
foreach ($file in $sqlFiles) {
    Write-Host "  - $($file.Name)" -ForegroundColor Gray
}
Write-Host ""

# Executa cada arquivo SQL em ordem
foreach ($file in $sqlFiles) {
    Write-Host "Executando: $($file.Name)" -ForegroundColor Cyan
    
    try {
        # Substitua pela sua string de conexão e comando apropriado
        
        # SQL Server:
        sqlcmd -S "servidor" -d "database" -i $file.FullName
        
        # MySQL:
        # mysql -u usuario -p database < $file.FullName
        
        # PostgreSQL:
        # psql -U usuario -d database -f $file.FullName
        
        Write-Host "✓ $($file.Name) executado com sucesso" -ForegroundColor Green
    }
    catch {
        Write-Host "✗ Erro ao executar $($file.Name): $($_.Exception.Message)" -ForegroundColor Red
        # Para em caso de erro para manter a integridade da sequência
        Write-Host "Execução interrompida devido ao erro acima." -ForegroundColor Red
        exit 1
    }
}

Write-Host "Execução dos seeds concluída!" -ForegroundColor Green


$inputPath = "\\wsl.localhost\Ubuntu\home\gaa\repo\miyakoya\assets\Gemini_Generated_Image_qr20ftqr20ftqr20.png"
$outputPath = "\\wsl.localhost\Ubuntu\home\gaa\repo\miyakoya\assets\hero_bg_optimized.jpg"

Add-Type -AssemblyName System.Drawing

try {
    $image = [System.Drawing.Image]::FromFile($inputPath)
    
    $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, 85) # Quality 85

    $image.Save($outputPath, $codec, $encoderParams)
    
    Write-Host "Image optimized successfully!"
    $inSize = (Get-Item $inputPath).Length / 1MB
    $outSize = (Get-Item $outputPath).Length / 1MB
    Write-Host ("Original: {0:N2} MB" -f $inSize)
    Write-Host ("Optimized: {0:N2} MB" -f $outSize)
}
catch {
    Write-Error $_.Exception.Message
}
finally {
    if ($image) { $image.Dispose() }
}

function Expand-Tab {
  param([UInt32] $TabWidth = 4)
  process {
    $line = $_
    while ( $TRUE ) {
  $i = $line.IndexOf([Char] 9)
  if ( $i -eq -1 ) { break }
  if ( $TabWidth -gt 0 ) {
    $pad = " " * ($TabWidth - ($i % $TabWidth))
  } else {
    $pad = ""
  }
  $line = $line -replace "^([^\t]{$i})\t(.*)$",
    "`$1$pad`$2"
    }
    $line
  }
}

Get-ChildItem -Recurse *.py | ForEach-Object { (Get-Content $_ | Expand-Tab) | Set-Content $_ }
Get-ChildItem -Recurse *.py | ForEach-Object { (Get-Content $_ | ForEach-Object { $_.TrimEnd() }) | Set-Content $_ }

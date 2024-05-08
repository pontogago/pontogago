// Selecionar a pasta onde estão as imagens
var inputFolder = Folder.selectDialog("Selecione a pasta com as imagens");

// Verificar se uma pasta foi selecionada
if (inputFolder != null) {
    // Selecionar a pasta onde as imagens editadas serão salvas
    var outputFolder = Folder.selectDialog("Selecione a pasta para salvar as imagens editadas");
    
    // Verificar se uma pasta foi selecionada
    if (outputFolder != null) {
        // Listar todos os arquivos na pasta de entrada
        var files = inputFolder.getFiles();
        
        // Loop através de cada arquivo na pasta de entrada
        for (var i = 0; i < files.length; i++) {
            // Verificar se o arquivo é uma imagem
            if (files[i] instanceof File && files[i].name.match(/\.(jpg|jpeg|png|gif)$/i)) {
                // Abrir a imagem no Photoshop
                var doc = app.open(files[i]);
                
                // Aplicar a máscara de nitidez
                app.activeDocument.activeLayer.applyUnSharpMask(150, 3.0, 11);
                
                // Salvar a imagem editada na pasta de saída como JPEG
                var jpgOptions = new JPEGSaveOptions();
                jpgOptions.quality = 10; // Qualidade da imagem JPEG (0-12)
                var outputFile = new File(outputFolder + "/" + doc.name.replace(/\.[^\.]+$/, '.jpg'));
                doc.saveAs(outputFile, jpgOptions, true);
                
                // Fechar o documento sem salvar as alterações no original
                doc.close(SaveOptions.DONOTSAVECHANGES);
            }
        }
        alert("Processo concluído. As imagens foram editadas e salvas na pasta especificada como JPEG.");
    } else {
        alert("Nenhuma pasta de saída selecionada. O processo foi interrompido.");
    }
} else {
    alert("Nenhuma pasta de entrada selecionada. O processo foi interrompido.");
}

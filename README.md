# MH_Mark_Tool
a mark tool for a game named MHXY.

# train tesseract ocr
# not to use * in powershell
# anyway, to train a suitable model, it needs a too long time unexpectedly.
java --module-path javafx-sdk-21/lib --add-modules javafx.controls,javafx.fxml -cp jTessBoxEditorFX.jar;javafx-sdk-21/lib/* net.sourceforge.tessboxeditor.JTessBoxEditor

# now, to determine to use paddleocr
# it can promise the accuracy, but the speed is not very quick.
# To make it faster, there are some measures needed.


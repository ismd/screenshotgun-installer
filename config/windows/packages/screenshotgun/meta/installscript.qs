function Component() {
}

Component.prototype.createOperations = function() {
    component.createOperations();
    component.addOperation("CreateShortcut", "@TargetDir@/screenshotgun.exe", "@StartMenuDir@/screenshotgun.lnk", "workingDirectory=@TargetDir@", "iconPath=@TargetDir@/screenshotgun.ico");
}

function Controller() {
}

Controller.prototype.IntroductionPageCallback = function() {
    if (installer.isUpdater()) {
        gui.clickButton(buttons.NextButton);
    }
}

Controller.prototype.ComponentSelectionPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.ReadyForInstallationPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.FinishedPageCallback = function() {
    if (installer.isUpdater()) {
        var widget = gui.currentPageWidget();
        widget.RunItCheckBox.checked = false;
        gui.clickButton(buttons.FinishButton);
    }
}

#include <iostream>

using namespace std;


int main(void) {
    cout << "Welcome to the Incredible Installation Wizard, a"
         << endl
         << "package installation manager written in C++ by Dante"
         << endl
         << "Falzone for the videogame DEBUGGER."
         << endl
         << "To continue, please enter a password with sudo/admin"
         << endl
         << "privileges and press ENTER.\n";
    string password;
    cin >> password;
    cin.ignore(255,'\n'); //Who on earth has a password more than 255 chars long? Not even Julian Assange
    cout << "Loading.";
    system(("echo \"" + password + "\" | sudo -S apt-get -y install python3").c_str());
    system(("echo \"" + password + "\" | sudo -S -k easy_install python3").c_str());
    // Above line sends commands for both Mac OS X and Linux
    system(("echo \"" + password + "\" | sudo -S -k easy_install python3-pip").c_str());
    system(("echo \"" + password + "\" | sudo -S -k apt-get -y install python3-pip").c_str());
    cout << ".";
    system("pip3 install pygame");
    system(("echo \"" + password + "\" | sudo -S -k easy_install sox").c_str());
    system(("echo \"" + password + "\" | sudo -S -k apt-get -y install sox").c_str());
    /*
     * Haven't actually tried this on a Mac, but
     * I'm reasonably sure that it will work. I
     * believe I read somewhere that the Mac
     * equivalent of `apt-get install` is `easy-
     * install`. ~ 22 Feb 2019
     */
    system(("echo \"" + password + "\" | sudo -S -k easy-install zenity").c_str());
    cout << ".";
    system("brew install homebrew/x11/zenity"); // so that the GUI will work on Mac
    system("cd ~/Desktop/Debugger_v2_portable");
    system(("echo \"" + password + "\" | sudo -S -k install hackerman.ttf ~/Library/Fonts").c_str()); // for mac
    system(("echo \"" + password + "\" | sudo -S -k install hackerman.ttf /lib/fonts").c_str()); // for linux
    system("zenity --info --title=\"DEBUGGER Installation\" --text=\"The installation is complete. Type 'cd ~/Desktop/Debugger_v2_portable &amp;&amp; python3 ./useof.py' in the Terminal and press ENTER to play the game.\" --width=300");
    //above line sends a GUI dialog box
    return 0;
}
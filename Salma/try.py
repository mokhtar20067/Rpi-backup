import io
import picamera
import logging
import socketserver
from evdev import InputDevice
from threading import Condition
from http import server
import threading, os, signal
import subprocess
from subprocess import check_call, call
import sys
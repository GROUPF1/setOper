# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('kishor')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('kishor')

import os
import sys
from msdialog import msdialog
import subprocess

from kishor_lib import Window
from kishor.AboutKishorDialog import AboutKishorDialog
from kishor.PreferencesKishorDialog import PreferencesKishorDialog

# See kishor_lib.Window.py for more details about how this class works
class KishorWindow(Window):
    __gtype_name__ = "KishorWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(KishorWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutKishorDialog
        self.PreferencesDialog = PreferencesKishorDialog

        # Code for other initialization actions should be added here.
    def on_setm_clicked(self,widget,data=None):
        print "Set_Membership"
        y="grep -xc ";
        t1=self.ui.entry1.get_text()
        t2=self.ui.entry2.get_text()
        y=y+"'"+t1+"'"+" "+t2
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
#            elif response == Gtk.ResponseType.OK:
#                self.ui.ip1.set_text(" ")
#                self.ui.ip2.set_text(" ")
        w.destroy()


#diff -q <(sort set1 | uniq) <(sort set2 | uniq)
        # Code for other initialization actions should be added here.
    def on_equality_clicked(self,widget,data=None):
        print "Set Equality"
        t1=self.ui.entry1.get_text()
        t2=self.ui.entry2.get_text()

        s1="sort "+t1+" | uniq";
        s2="sort "+t2+" | uniq";
        print "heyyy"
        result1 = os.system(s1)
        result2 = os.system(s2)
        fil1=open("f1.txt","w");
        fil2=open("f2.txt","w");
        f1.write(result1);
        f2.write(result2);
        f1.close();
        f2.close();
        y="diff "+"f1.txt "+"f2.txt";
        y
        result=os.system(y) 
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
        w.destroy()

# wc -l set | cut -d' ' -f1

#set cardinality
    def on_setcardi_clicked(self,widget,data=None):
        print "Set_cardinality"
        y="wc -l ";
        t1=self.ui.entry1.get_text()
        
        y=y+t1+" | cut -d' ' -f1"
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
#            elif response == Gtk.ResponseType.OK:
#                self.ui.ip1.set_text(" ")
#                self.ui.ip2.set_text(" ")
        w.destroy()

#comm -23 <(sort subset | uniq) <(sort set | uniq) | head -1
#subset
    def on_subset_clicked(self,widget,data=None):
        print "Subset Operation"
        y="comm -23 <(sort ";
        t1=self.ui.entry1.get_text()
        t2=self.ui.entry2.get_text()
        y=y+t1+" | uniq) <(sort "+t2+" | uniq) | head -1"
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
        w.destroy()

#$ cat set1 set2
#set concat

    def on_setconcat_clicked(self,widget,data=None):
        print "Set Concatination"
        y="cat ";
        t1=self.ui.entry1.get_text()
        t2=self.ui.entry2.get_text()
        y=y+t1+" "+t2
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
        w.destroy()

#$ comm -12 <(sort set1) <(sort set2)
#set intersection

    def on_setintersect_clicked(self,widget,data=None):
        print "Set_Intersection"
        y="comm -12 <(sort ";
        t1="Dataset1"
        t2="Dataset2"
        y=y+t1+") <(sort "+t2+")"
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
        w.destroy()

#$ grep -vxF -f set2 set1
#set complement

    def on_setcomp_clicked(self,widget,data=None):
        print "Set Complement"
        y="grep -vxF -f ";
        t1=self.ui.entry1.get_text()
        t2=self.ui.entry2.get_text()
        y=y+t1+" "+t2
        result=os.system(y)
        a=os.popen(y).read()
        print result
        w=msdialog(self,a)
        response=w.run()
        if response == Gtk.ResponseType.CLOSE :
            sys.exit()
        w.destroy()


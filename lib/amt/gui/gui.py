import os
import sys
import wx
import wx.aui
import wx.lib.newevent
import logging

__all__ = ['gui']
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

from amt.load import load
sys.path.insert(0, dirName)
import images


class wxLogHandler(logging.Handler):
    """
    A handler class which sends log strings to a wx object
    """
    wxLogEvent, EVT_WX_LOG_EVENT = wx.lib.newevent.NewEvent()

    def __init__(self, wxDest=None):
        """
        Initialize the handler
        @param wxDest: the destination object to post the event to
        @type wxDest: wx.Window
        """
        logging.Handler.__init__(self)
        self.wxDest = wxDest
        self.level = logging.DEBUG

    def flush(self):
        """
        does nothing for this handler
        """
        pass

    def emit(self, record):
        """
        Emit a record.

        """
        try:
            msg = self.format(record)
            evt = self.wxLogEvent(message=msg, levelname=record.levelname)
            wx.PostEvent(self.wxDest, evt)
        except (KeyboardInterrupt, SystemExit):
            raise


class MainFrame(wx.Frame):

    def __init__(self, parent, id=-1, title='AMT',
                 pos=wx.DefaultPosition, size=(800, 600),
                 style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        # Create a logger for this class
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
        handler = wxLogHandler(self)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"))
        # self.log.addHandler(handler)
        logger = logging.getLogger()
        logger.addHandler(handler)

        # Create Menu
        self.InitUI()

        self._mgr = wx.aui.AuiManager(self)

        # create several text controls
        self.image_list = wx.ImageList(16, 16, True, 2)
        self.folder_image = self.image_list.Add(wx.ArtProvider.GetBitmap(
            wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        self.file_list_image = self.image_list.Add(wx.ArtProvider.GetBitmap(
            wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        self.file_dictionary_image = self.image_list.Add(
            wx.ArtProvider.GetBitmap(
                wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(16, 16)))
        self.list_image = self.image_list.Add(wx.ArtProvider.GetBitmap(
            wx.ART_LIST_VIEW, wx.ART_OTHER, wx.Size(16, 16)))
        self.dictionary_image = self.image_list.Add(wx.ArtProvider.GetBitmap(
            wx.ART_REPORT_VIEW, wx.ART_OTHER, wx.Size(16, 16)))
        self.record_image = self.image_list.Add(wx.ArtProvider.GetBitmap(
            wx.ART_EXECUTABLE_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        self.tree = self.CreateTreeCtrl()

        text2 = wx.TextCtrl(self, -1, '',
                            wx.DefaultPosition, wx.Size(200, 150),
                            wx.NO_BORDER | wx.TE_MULTILINE | wx.TE_READONLY |
                            wx.HSCROLL)

        text3 = wx.TextCtrl(self, -1, 'Main content window',
                            wx.DefaultPosition, wx.Size(200, 150),
                            wx.NO_BORDER | wx.TE_MULTILINE)
        self.logconsole = text2

        # add the panes to the manager
        self._mgr.AddPane(self.tree, wx.LEFT, 'Artifact Tree')
        self._mgr.AddPane(text2, wx.BOTTOM, 'Log Console')
        self._mgr.AddPane(text3, wx.CENTER)

        # tell the manager to 'commit' all the changes just made
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wxLogHandler.EVT_WX_LOG_EVENT, self.onLogEvent)

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        new_button = fileMenu.Append(
            wx.ID_NEW, '&New\tCtrl+N', 'Create a new session')
        open_button = fileMenu.Append(
            wx.ID_OPEN, '&Open\tCtrl+O', 'Open a new location')
        save_button = fileMenu.Append(
            wx.ID_SAVE, '&Save\tCtrl+S', 'Save to current location')
        save_as_button = fileMenu.Append(
            wx.ID_SAVEAS, 'Save &As\tCtrl+A', 'Save to a new location')

        fileMenu.AppendSeparator()

        quit_button = fileMenu.Append(
            wx.ID_EXIT, '&Quit\tCtrl+Q', 'Exit the application')

        # Bind Events
        self.Bind(wx.EVT_MENU, self.OnNew, new_button)
        self.Bind(wx.EVT_MENU, self.OnOpen, open_button)
        self.Bind(wx.EVT_MENU, self.OnSave, save_button)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, save_as_button)
        self.Bind(wx.EVT_MENU, self.OnClose, quit_button)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

    def OnNew(self, e):
        LOGGER.info("New")

    def OnOpen(self, e):
        LOGGER.info("Open")

    def OnSave(self, e):
        LOGGER.info("Save")

    def OnSaveAs(self, e):
        LOGGER.info("Save As")

    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        tree.AssignImageList(self.image_list)

        def _addbranch(node, branch):
            for key, value in branch.items():
                if key.startswith('_'):
                    continue
                if isinstance(value, dict):
                    if '__file__' in value:
                        # TODO: switch between file_list_image and
                        # file_dictionary_image
                        image = self.file_list_image
                    else:
                        image = self.folder_image
                    sub_node = tree.AppendItem(node, key, image)
                    _addbranch(sub_node, value)
                elif isinstance(value, (tuple, list, set)):
                    sub_node = tree.AppendItem(node, key, self.list_image)
                    # for item in value:
                    #     _addbranch(sub_node, value)
                else:
                    sub_node = tree.AppendItem(node, key, self.record_image)
        artifacts = 'pm'
        root = tree.AddRoot(os.path.basename(artifacts), self.folder_image)
        artifacts = load(artifacts)
        _addbranch(root, artifacts)
        tree.Expand(root)
        return tree

    def onLogEvent(self, event):
        msg = event.message.strip("\r") + "\n"
        self.logconsole.AppendText(msg)
        event.Skip()

    def OnClose(self, event):
        # deinitialize the frame manager
        self._mgr.UnInit()

        # delete the frame
        self.Destroy()


def gui():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

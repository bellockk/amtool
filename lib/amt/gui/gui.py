import os
import sys
import random
import wx
import wx.html
import wx.grid

__all__ = ['gui']

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError:  # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_SwitchPane = ID_CreateTree + 12
ID_CreatePerspective = ID_CreateTree + 13
ID_CopyPerspectiveCode = ID_CreateTree + 14
ID_CreateNBPerspective = ID_CreateTree + 15
ID_CopyNBPerspectiveCode = ID_CreateTree + 16
ID_AllowFloating = ID_CreateTree + 17
ID_AllowActivePane = ID_CreateTree + 18
ID_TransparentHint = ID_CreateTree + 19
ID_VenetianBlindsHint = ID_CreateTree + 20
ID_RectangleHint = ID_CreateTree + 21
ID_NoHint = ID_CreateTree + 22
ID_HintFade = ID_CreateTree + 23
ID_NoVenetianFade = ID_CreateTree + 24
ID_TransparentDrag = ID_CreateTree + 25
ID_NoGradient = ID_CreateTree + 26
ID_VerticalGradient = ID_CreateTree + 27
ID_HorizontalGradient = ID_CreateTree + 28
ID_LiveUpdate = ID_CreateTree + 29
ID_AnimateFrames = ID_CreateTree + 30
ID_TransparentPane = ID_CreateTree + 32
ID_DefaultDockArt = ID_CreateTree + 33
ID_ModernDockArt = ID_CreateTree + 34
ID_SnapToScreen = ID_CreateTree + 35
ID_SnapPanes = ID_CreateTree + 36
ID_FlyOut = ID_CreateTree + 37
ID_Settings = ID_CreateTree + 39
ID_CustomizeToolbar = ID_CreateTree + 40
ID_DropDownToolbarItem = ID_CreateTree + 41
ID_MinimizePosSmart = ID_CreateTree + 42
ID_MinimizePosTop = ID_CreateTree + 43
ID_MinimizePosLeft = ID_CreateTree + 44
ID_MinimizePosRight = ID_CreateTree + 45
ID_MinimizePosBottom = ID_CreateTree + 46
ID_MinimizeCaptSmart = ID_CreateTree + 47
ID_MinimizeCaptHorz = ID_CreateTree + 48
ID_MinimizeCaptHide = ID_CreateTree + 49
ID_NotebookNoCloseButton = ID_CreateTree + 50
ID_NotebookCloseButton = ID_CreateTree + 51
ID_NotebookCloseButtonAll = ID_CreateTree + 52
ID_NotebookCloseButtonActive = ID_CreateTree + 53
ID_NotebookCloseOnLeft = ID_CreateTree + 54
ID_NotebookAllowTabMove = ID_CreateTree + 55
ID_NotebookAllowTabExternalMove = ID_CreateTree + 56
ID_NotebookAllowTabSplit = ID_CreateTree + 57
ID_NotebookTabFloat = ID_CreateTree + 58
ID_NotebookTabDrawDnd = ID_CreateTree + 59
ID_NotebookDclickUnsplit = ID_CreateTree + 60
ID_NotebookWindowList = ID_CreateTree + 61
ID_NotebookScrollButtons = ID_CreateTree + 62
ID_NotebookTabFixedWidth = ID_CreateTree + 63
ID_NotebookArtGloss = ID_CreateTree + 64
ID_NotebookArtSimple = ID_CreateTree + 65
ID_NotebookArtVC71 = ID_CreateTree + 66
ID_NotebookArtFF2 = ID_CreateTree + 67
ID_NotebookArtVC8 = ID_CreateTree + 68
ID_NotebookArtChrome = ID_CreateTree + 69
ID_NotebookAlignTop = ID_CreateTree + 70
ID_NotebookAlignBottom = ID_CreateTree + 71
ID_NotebookHideSingle = ID_CreateTree + 72
ID_NotebookSmartTab = ID_CreateTree + 73
ID_NotebookUseImagesDropDown = ID_CreateTree + 74
ID_NotebookMinMaxWidth = ID_CreateTree + 76

ID_SampleItem = ID_CreateTree + 77
ID_StandardGuides = ID_CreateTree + 78
ID_AeroGuides = ID_CreateTree + 79
ID_WhidbeyGuides = ID_CreateTree + 80
ID_NotebookPreview = ID_CreateTree + 81
ID_PreviewMinimized = ID_CreateTree + 82

ID_SmoothDocking = ID_CreateTree + 83
ID_NativeMiniframes = ID_CreateTree + 84

ID_FirstPerspective = ID_CreatePerspective + 1000
ID_FirstNBPerspective = ID_CreateNBPerspective + 10000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColour = ID_PaneBorderSize + 4
ID_SashColour = ID_PaneBorderSize + 5
ID_InactiveCaptionColour = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColour = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColour = ID_PaneBorderSize + 8
ID_ActiveCaptionColour = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColour = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColour = ID_PaneBorderSize + 11
ID_BorderColour = ID_PaneBorderSize + 12
ID_GripperColour = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14

ID_VetoTree = ID_PaneBorderSize + 15
ID_VetoText = ID_PaneBorderSize + 16
ID_NotebookMultiLine = ID_PaneBorderSize + 17


class SizeReportCtrl(wx.PyControl):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, mgr=None):

        wx.PyControl.__init__(self, parent, id, pos, size, style=wx.NO_BORDER)
        self._mgr = mgr

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):

        dc = wx.PaintDC(self)
        size = self.GetClientSize()

        s = "Size: %d x %d" % (size.x, size.y)

        dc.SetFont(wx.NORMAL_FONT)
        w, height = dc.GetTextExtent(s)
        height += 3
        dc.SetBrush(wx.WHITE_BRUSH)
        dc.SetPen(wx.WHITE_PEN)
        dc.DrawRectangle(0, 0, size.x, size.y)
        dc.SetPen(wx.LIGHT_GREY_PEN)
        dc.DrawLine(0, 0, size.x, size.y)
        dc.DrawLine(0, size.y, size.x, 0)
        dc.DrawText(s, (size.x-w)/2, (size.y-height*5)/2)

        if self._mgr:

            pi = self._mgr.GetPane(self)

            s = "Layer: %d" % pi.dock_layer
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*1))

            s = "Dock: %d Row: %d" % (pi.dock_direction, pi.dock_row)
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*2))

            s = "Position: %d" % pi.dock_pos
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*3))

            s = "Proportion: %d" % pi.dock_proportion
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*4))

    def OnEraseBackground(self, event):

        pass

    def OnSize(self, event):

        self.Refresh()


class SettingsPanel(wx.Panel):

    def __init__(self, parent, frame):

        wx.Panel.__init__(self, parent)
        self._frame = frame

        s1 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_size = wx.SpinCtrl(
            self, ID_PaneBorderSize, "%d" % frame.GetDockArt().GetMetric(
                aui.AUI_DOCKART_PANE_BORDER_SIZE),
            wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
            frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.Add(wx.StaticText(self, -1, "Pane Border Size:"))
        s1.Add(self._border_size)
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.SetItemMinSize(1, (180, 20))

        s2 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_size = wx.SpinCtrl(
            self, ID_SashSize, "%d" % frame.GetDockArt().GetMetric(
                aui.AUI_DOCKART_SASH_SIZE), wx.DefaultPosition,
            wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
            frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.Add(wx.StaticText(self, -1, "Sash Size:"))
        s2.Add(self._sash_size)
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.SetItemMinSize(1, (180, 20))

        s3 = wx.BoxSizer(wx.HORIZONTAL)
        self._caption_size = wx.SpinCtrl(
            self, ID_CaptionSize, "%d" % frame.GetDockArt().GetMetric(
                aui.AUI_DOCKART_CAPTION_SIZE),
            wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
            frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.Add(wx.StaticText(self, -1, "Caption Size:"))
        s3.Add(self._caption_size)
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.SetItemMinSize(1, (180, 20))

        b = self.CreateColourBitmap(wx.BLACK)

        s4 = wx.BoxSizer(wx.HORIZONTAL)
        self._background_colour = wx.BitmapButton(
            self, ID_BackgroundColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.Add(wx.StaticText(self, -1, "Background Colour:"))
        s4.Add(self._background_colour)
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.SetItemMinSize(1, (180, 20))

        s5 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_colour = wx.BitmapButton(
            self, ID_SashColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.Add(wx.StaticText(self, -1, "Sash Colour:"))
        s5.Add(self._sash_colour)
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.SetItemMinSize(1, (180, 20))

        s6 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_colour = wx.BitmapButton(
            self, ID_InactiveCaptionColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.Add(wx.StaticText(self, -1, "Normal Caption:"))
        s6.Add(self._inactive_caption_colour)
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.SetItemMinSize(1, (180, 20))

        s7 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_gradient_colour = wx.BitmapButton(
            self, ID_InactiveCaptionGradientColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.Add(wx.StaticText(self, -1, "Normal Caption Gradient:"))
        s7.Add(self._inactive_caption_gradient_colour)
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.SetItemMinSize(1, (180, 20))

        s8 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_text_colour = wx.BitmapButton(
            self, ID_InactiveCaptionTextColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.Add(wx.StaticText(self, -1, "Normal Caption Text:"))
        s8.Add(self._inactive_caption_text_colour)
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.SetItemMinSize(1, (180, 20))

        s9 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_colour = wx.BitmapButton(
            self, ID_ActiveCaptionColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.Add(wx.StaticText(self, -1, "Active Caption:"))
        s9.Add(self._active_caption_colour)
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.SetItemMinSize(1, (180, 20))

        s10 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_gradient_colour = wx.BitmapButton(
            self, ID_ActiveCaptionGradientColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.Add(wx.StaticText(self, -1, "Active Caption Gradient:"))
        s10.Add(self._active_caption_gradient_colour)
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.SetItemMinSize(1, (180, 20))

        s11 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_text_colour = wx.BitmapButton(
            self, ID_ActiveCaptionTextColour, b, wx.DefaultPosition,
            wx.Size(50, 25))
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.Add(wx.StaticText(self, -1, "Active Caption Text:"))
        s11.Add(self._active_caption_text_colour)
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.SetItemMinSize(1, (180, 20))

        s12 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_colour = wx.BitmapButton(
            self, ID_BorderColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.Add(wx.StaticText(self, -1, "Border Colour:"))
        s12.Add(self._border_colour)
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.SetItemMinSize(1, (180, 20))

        s13 = wx.BoxSizer(wx.HORIZONTAL)
        self._gripper_colour = wx.BitmapButton(
            self, ID_GripperColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.Add(wx.StaticText(self, -1, "Gripper Colour:"))
        s13.Add(self._gripper_colour)
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.SetItemMinSize(1, (180, 20))

        s14 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_grip = wx.CheckBox(
            self, ID_SashGrip, "", wx.DefaultPosition, wx.Size(50, 20))
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.Add(wx.StaticText(self, -1, "Draw Sash Grip:"))
        s14.Add(self._sash_grip)
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.SetItemMinSize(1, (180, 20))

        grid_sizer = wx.GridSizer(0, 2)
        grid_sizer.SetHGap(5)
        grid_sizer.Add(s1)
        grid_sizer.Add(s4)
        grid_sizer.Add(s2)
        grid_sizer.Add(s5)
        grid_sizer.Add(s3)
        grid_sizer.Add(s13)
        grid_sizer.Add(s14)
        grid_sizer.Add((1, 1))
        grid_sizer.Add(s12)
        grid_sizer.Add(s6)
        grid_sizer.Add(s9)
        grid_sizer.Add(s7)
        grid_sizer.Add(s10)
        grid_sizer.Add(s8)
        grid_sizer.Add(s11)

        cont_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(cont_sizer)
        self.GetSizer().SetSizeHints(self)

        self._border_size.SetValue(frame.GetDockArt().GetMetric(
            aui.AUI_DOCKART_PANE_BORDER_SIZE))
        self._sash_size.SetValue(frame.GetDockArt().GetMetric(
            aui.AUI_DOCKART_SASH_SIZE))
        self._caption_size.SetValue(frame.GetDockArt().GetMetric(
            aui.AUI_DOCKART_CAPTION_SIZE))
        self._sash_grip.SetValue(frame.GetDockArt().GetMetric(
            aui.AUI_DOCKART_DRAW_SASH_GRIP))

        self.UpdateColours()

        self.Bind(wx.EVT_SPINCTRL, self.OnPaneBorderSize, id=ID_PaneBorderSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnSashSize, id=ID_SashSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnCaptionSize, id=ID_CaptionSize)
        self.Bind(wx.EVT_CHECKBOX, self.OnDrawSashGrip, id=ID_SashGrip)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BackgroundColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_SashColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour,
                  id=ID_InactiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour,
                  id=ID_InactiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour,
                  id=ID_ActiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour,
                  id=ID_ActiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour,
                  id=ID_ActiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BorderColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_GripperColour)

    def CreateColourBitmap(self, c):

        image = wx.EmptyImage(25, 14)
        for x in xrange(25):
            for y in xrange(14):
                pixcol = c
                if x == 0 or x == 24 or y == 0 or y == 13:
                    pixcol = wx.BLACK

                image.SetRGB(x, y, pixcol.Red(), pixcol.Green(), pixcol.Blue())

        return image.ConvertToBitmap()

    def UpdateColours(self):

        bk = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_BACKGROUND_COLOUR)
        self._background_colour.SetBitmapLabel(self.CreateColourBitmap(bk))

        cap = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR)
        self._inactive_caption_colour.SetBitmapLabel(
            self.CreateColourBitmap(cap))

        capgrad = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR)
        self._inactive_caption_gradient_colour.SetBitmapLabel(
            self.CreateColourBitmap(capgrad))

        captxt = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR)
        self._inactive_caption_text_colour.SetBitmapLabel(
            self.CreateColourBitmap(captxt))

        acap = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR)
        self._active_caption_colour.SetBitmapLabel(
            self.CreateColourBitmap(acap))

        acapgrad = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR)
        self._active_caption_gradient_colour.SetBitmapLabel(
            self.CreateColourBitmap(acapgrad))

        acaptxt = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR)
        self._active_caption_text_colour.SetBitmapLabel(
            self.CreateColourBitmap(acaptxt))

        sash = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_SASH_COLOUR)
        self._sash_colour.SetBitmapLabel(self.CreateColourBitmap(sash))

        border = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_BORDER_COLOUR)
        self._border_colour.SetBitmapLabel(self.CreateColourBitmap(border))

        gripper = self._frame.GetDockArt().GetColour(
            aui.AUI_DOCKART_GRIPPER_COLOUR)
        self._gripper_colour.SetBitmapLabel(self.CreateColourBitmap(gripper))

    def OnPaneBorderSize(self, event):

        self._frame.GetDockArt().SetMetric(
            aui.AUI_DOCKART_PANE_BORDER_SIZE, event.GetInt())
        self._frame.DoUpdate()

    def OnSashSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_SASH_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()

    def OnCaptionSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_CAPTION_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()

    def OnDrawSashGrip(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP,
                                           event.GetInt())
        self._frame.DoUpdate()

    def OnSetColour(self, event):

        dlg = wx.ColourDialog(self._frame)
        dlg.SetTitle("Colour Picker")

        if dlg.ShowModal() != wx.ID_OK:
            return

        evId = event.GetId()
        if evId == ID_BackgroundColour:
            var = aui.AUI_DOCKART_BACKGROUND_COLOUR
        elif evId == ID_SashColour:
            var = aui.AUI_DOCKART_SASH_COLOUR
        elif evId == ID_InactiveCaptionColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR
        elif evId == ID_InactiveCaptionGradientColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_InactiveCaptionTextColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_ActiveCaptionColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR
        elif evId == ID_ActiveCaptionGradientColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_ActiveCaptionTextColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_BorderColour:
            var = aui.AUI_DOCKART_BORDER_COLOUR
        elif evId == ID_GripperColour:
            var = aui.AUI_DOCKART_GRIPPER_COLOUR
        else:
            return

        self._frame.GetDockArt().SetColour(
            var, dlg.GetColourData().GetColour())
        self._frame.DoUpdate()
        self.UpdateColours()


class CustomDataTable(wx.grid.PyGridTableBase):
    def __init__(self, log):
        wx.grid.PyGridTableBase.__init__(self)
        self.log = log
        self.filename = None
        self.file_data = []
        self.data = []
        self.col_properties = []
        self.colLabels = []
        self.hidden_cols = []
        self.hidden_rows = []
        self.filters = {}
        self.type_map = {
            'NUMBER': wx.grid.GRID_VALUE_NUMBER,
            'STRING': wx.grid.GRID_VALUE_STRING,
            'CHOICE': wx.grid.GRID_VALUE_CHOICE,
            'BOOL': wx.grid.GRID_VALUE_BOOL,
            'FLOAT': wx.grid.GRID_VALUE_FLOAT}

    # required methods for the wxPyGridTableBase interface
    def GetTypeName(self, row, col):
        label = self.colLabels[col]
        for prop in self.col_properties:
            if prop['Name'] == label:
                if 'Type' in prop:
                    if prop['Type'] == 'CHOICE' and 'Choices' in prop:
                        return wx.grid.GRID_VALUE_CHOICE + ':' + ','.join(
                            prop['Choices'])
                    else:
                        return self.type_map[prop['Type']]
        return wx.grid.GRID_VALUE_STRING

    def Load(self, filename):

        # Notify the grid
        grid = self.GetView()
        grid.BeginBatch()
        msg = wx.grid.GridTableMessage(
            self, wx.grid.GRIDTABLE_NOTIFY_COLS_DELETED, 1,
            self.GetNumberCols())

        grid.ProcessTableMessage(msg)
        msg = wx.grid.GridTableMessage(
            self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, 1,
            self.GetNumberRows())
        grid.ProcessTableMessage(msg)

        grid.EndBatch()

        self.filename = filename
        with open(filename, 'r') as f:
            data = safe_load(f)

        self.file_data = data['Artifacts']
        self.data = [d for d in self.file_data]
        self.col_properties = data['Metadata']['ColumnProperties']

        # Get column labels
        self.colLabels = [c['Name'] for c in self.col_properties]

        # Notify the grid
        grid.BeginBatch()
        msg = wx.grid.GridTableMessage(
            self, wx.grid.GRIDTABLE_NOTIFY_COLS_APPENDED,
            self.GetNumberCols())

        grid.ProcessTableMessage(msg)
        msg = wx.grid.GridTableMessage(
            self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED, self.GetNumberRows())

        grid.ProcessTableMessage(msg)
        grid.EndBatch()

    def Save(self):
        self.SaveAs(self.filename)

    def SaveAs(self, filename):
        self.filename = filename
        write_dict = OrderedDict()
        write_dict['Metadata'] = {'ColumnProperties': self.col_properties}
        write_dict['Artifacts'] = self.file_data
        with open(filename, 'w') as f:
            f.write(safe_dump(write_dict, default_flow_style=False))

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return not self.data[row][self.colLabels[col]]

    def GetValue(self, row, col):
        return self.data[row][self.colLabels[col]]

    def SetValue(self, row, col, value):
        self.data[row][self.colLabels[col]] = value

    # Some optional methods

    # Called when the grid needs to display column labels
    def GetColLabelValue(self, col):
        return self.colLabels[col]

    # Called when the grid needs to display row labels
    # def GetRowLabelValue(self, row):
    #     return self.rowLabels[row]

    # Methods added for demo purposes.

    # The physical moving of the cols/rows is left to the implementer.
    # Because of the dynamic nature of a wxGrid the physical moving of
    # columns differs from implementation to implementation

    # Move the column
    def MoveColumn(self, frm, to):
        grid = self.GetView()

        if grid:
            # Move the identifiers
            old = self.colLabels[frm]
            del self.colLabels[frm]

            if to > frm:
                self.colLabels.insert(to - 1, old)
            else:
                self.colLabels.insert(to, old)

            # Notify the grid
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_DELETED, frm, 1
                    )

            grid.ProcessTableMessage(msg)

            if to == self.GetNumberCols():
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_APPENDED, 1)
            else:
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_INSERTED, to, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    # Move the row
    def MoveRow(self, frm, to):
        grid = self.GetView()

        if grid:
            # Move the rowLabels and data rows
            oldData = self.data[frm]
            del self.data[frm]

            if to > frm:
                self.data.insert(to - 1, oldData)
            else:
                self.data.insert(to, oldData)

            # Notify the grid
            grid.BeginBatch()

            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, frm, 1)

            grid.ProcessTableMessage(msg)

            if to == self.GetNumberRows():
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED, 1)
            else:
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_ROWS_INSERTED, to, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def InsertRow(self, row):
        entry = {}
        for name in self.colLabels:
            entry[name] = ''
        ind = self.file_data.index(self.data[row])
        self.file_data.insert(ind, entry)
        self.data.insert(row, self.file_data[ind])
        grid = self.GetView()

        if grid:
            # Notify the grid
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                self, wx.grid.GRIDTABLE_NOTIFY_ROWS_INSERTED, row, 1)
            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def HideRows(self, rows):
        for row in rows:
            self.HideRow(row)

    def HideRow(self, row):
        grid = self.GetView()

        if grid:
            self.hidden_rows.append(
                [self.file_data.index(self.data[row]), row])
            del self.data[row]

            # Notify the grid
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, row, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def DeleteRows(self, rows):
        for row in rows:
            self.DeleteRow(row)

    def DeleteRow(self, row):
        grid = self.GetView()

        if grid:
            ind = self.file_data.index(self.data[row])
            del self.data[row]
            del self.file_data[ind]

            # Notify the grid
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, row, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def RenameCol(self, col, label):
        current_label = self.colLabels[col]
        self.colLabels[col] = label
        for r in self.data:
            if current_label in r:
                r[label] = r.pop(current_label)
        for r in self.file_data:
            if current_label in r:
                r[label] = r.pop(current_label)
        grid = self.GetView()
        if grid:
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_DELETED, col, 1
                    )

            grid.ProcessTableMessage(msg)

            if col == self.GetNumberCols():
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_APPENDED, 1)
            else:
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_INSERTED, col, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def InsertCol(self, col, label):
        self.colLabels.insert(col, label)
        for r in self.file_data:
            r[label] = ''
        grid = self.GetView()
        if grid:
            grid.BeginBatch()

            if col == self.GetNumberCols():
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_APPENDED, 1)
            else:
                msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_INSERTED, col, 1)

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def DeleteCols(self, cols):
        for col in cols:
            self.DeleteCol(col)

    def DeleteCol(self, col):
        label = self.colLabels[col]
        self.HideCol(col)
        for r in self.data:
            if label in r:
                del r[label]
        for r in self.file_data:
            if label in r:
                del r[label]

    def HideCols(self, cols):
        for col in cols:
            self.HideCol(col)

    def HideCol(self, col):
        grid = self.GetView()

        if grid:
            # Move the identifiers
            self.hidden_cols.append([self.colLabels[col], col])
            del self.colLabels[col]

            # Notify the grid
            grid.BeginBatch()
            msg = wx.grid.GridTableMessage(
                    self, wx.grid.GRIDTABLE_NOTIFY_COLS_DELETED, col, 1
                    )

            grid.ProcessTableMessage(msg)
            grid.EndBatch()

    def UnHideRows(self):
        grid = self.GetView()
        if grid:
            for ind, row in reversed(self.hidden_rows):
                if row == self.GetNumberRows():
                    self.data.append(self.file_data[ind])
                    msg = wx.grid.GridTableMessage(
                        self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED, 1)
                else:
                    self.data.insert(row, self.file_data[ind])
                    msg = wx.grid.GridTableMessage(
                        self, wx.grid.GRIDTABLE_NOTIFY_ROWS_INSERTED, row, 1)

                grid.ProcessTableMessage(msg)
                grid.EndBatch()
            self.hidden_rows = []
            self.filters = {}

    def UnHideCols(self):
        grid = self.GetView()
        if grid:
            # Un-Hide Columns
            for label, col in reversed(self.hidden_cols):
                if col == self.GetNumberCols():
                    self.colLabels.append(label)
                    msg = wx.grid.GridTableMessage(
                        self, wx.grid.GRIDTABLE_NOTIFY_COLS_APPENDED, 1)
                else:
                    self.colLabels.insert(col, label)
                    msg = wx.grid.GridTableMessage(
                        self, wx.grid.GRIDTABLE_NOTIFY_COLS_INSERTED, col, 1)

                grid.ProcessTableMessage(msg)
                grid.EndBatch()
            self.hidden_cols = []

    def UnHideAll(self):
        self.UnHideRows()
        self.UnHideCols()

    def ApplyFilters(self, col, filts):
        for filt in filts:
            self.ApplyFilter(col, filt)

    def ApplyFilter(self, col, filt):
        label = self.colLabels[col]
        # Was filter already selected
        if label in self.filters and filt in self.filters[label]:
            filters = [f for f in self.filters[label] if f != filt]
            self.RemoveFilterCol(col)
            self.ApplyFilters(col, filters)
        else:
            if label in self.filters:
                self.filters[label].append(filt)
            else:
                self.filters[label] = [filt]
            filters = self.filters[label]
            self.RemoveFilterCol(col)
            self.filters[label] = filters
            for i, r in reversed(list(enumerate(self.data))):
                if r[self.colLabels[col]] not in self.filters[label]:
                    self.HideRow(i)

    def RemoveFilterCols(self, cols):
        for col in cols:
            self.RemoveFilterCol(col)

    def RemoveFilterCol(self, col):
        filters = self.filters.copy()
        del filters[self.colLabels[col]]
        self.UnHideRows()
        for key, value in filters.iteritems():
            self.ApplyFilter(self.colLabels.index(key), value)


class DragableGrid(wx.grid.Grid):
    def __init__(self, parent, log):
        wx.grid.Grid.__init__(self, parent, -1)

        table = CustomDataTable(log)

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to
        # keep a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        # Enable Column moving
        gridmovers.GridColMover(self)
        self.Bind(gridmovers.EVT_GRID_COL_MOVE, self.OnColMove, self)

        # Enable Row moving
        gridmovers.GridRowMover(self)
        self.Bind(gridmovers.EVT_GRID_ROW_MOVE, self.OnRowMove, self)
        self.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,
                  self.OnLabelRightClick, self)

    def OnLabelRightClick(self, evt):
        row, col = evt.GetRow(), evt.GetCol()
        if row == -1:
            self.ColMenu(col, evt)
        if col == -1:
            self.RowMenu(row, evt)

    def RowMenu(self, row, evt):
        if not self.GetSelectedRows() or row not in self.GetSelectedRows():
            self.SelectRow(row)

        menu = wx.Menu()

        if len(self.GetSelectedRows()) == 1:
            insert = menu.Append(wx.ID_ANY, "Insert Row")
            self.Bind(
                wx.EVT_MENU, lambda event: self.GetTable().InsertRow(row),
                insert)
        delete = menu.Append(wx.ID_ANY, "Delete Row(s)")
        hide = menu.Append(wx.ID_ANY, "Hide Row(s)")

        self.Bind(wx.EVT_MENU, lambda event: self.GetTable().DeleteRows(
            self.GetSelectedRows()), delete)
        self.Bind(wx.EVT_MENU, lambda event: self.GetTable().HideRows(
            self.GetSelectedRows()), hide)

        self.PopupMenu(menu)
        menu.Destroy()

    def ColMenu(self, col, evt):
        if not self.GetSelectedCols() or col not in self.GetSelectedCols():
            self.SelectCol(col)
        menu = wx.Menu()
        if len(self.GetSelectedCols()) == 1:
            rename = menu.Append(wx.ID_ANY, "Rename Column Header")
            self.Bind(
                wx.EVT_MENU, lambda event: self.RenameCol(col),
                rename)
            insert = menu.Append(wx.ID_ANY, "Insert Column")
            self.Bind(
                wx.EVT_MENU, lambda event: self.InsertCol(col),
                insert)
        delete = menu.Append(wx.ID_ANY, "Delete Column(s)")
        hide = menu.Append(wx.ID_ANY, "Hide Column(s)")
        no_filt = menu.Append(wx.ID_ANY, "Remove Filter")
        if len(self.GetSelectedCols()) == 1:
            label = self.GetTable().colLabels[col]
            filters = self.GetTable().filters.get(label, [])
            file_data = self.GetTable().file_data
            unique = sorted(list(set(
                [r[label] for r in file_data if r[label]])))
            filt_menu = wx.Menu()
            filt_map = {}
            filt_list = []
            for u in unique:
                filt = filt_menu.Append(wx.ID_ANY, u, 'Filter by %s' % u,
                                        wx.ITEM_CHECK)
                if u in filters:
                    filt.Check()
                filt_list.append(filt.GetId())
                filt_map[filt.GetId()] = u
            self.Bind(wx.EVT_MENU_RANGE, lambda event:
                      self.GetTable().ApplyFilter(
                          col, filt_map[event.GetId()]), id=min(filt_list),
                      id2=max(filt_list))
            menu.AppendMenu(wx.ID_ANY, 'Filter', filt_menu)

        self.Bind(wx.EVT_MENU, lambda event: self.GetTable().DeleteCols(
            self.GetSelectedCols()), delete)
        self.Bind(wx.EVT_MENU, lambda event: self.GetTable().HideCols(
            self.GetSelectedCols()), hide)
        self.Bind(wx.EVT_MENU, lambda event: self.GetTable().RemoveFilterCols(
            self.GetSelectedCols()), no_filt)

        self.PopupMenu(menu)
        menu.Destroy()

    # Event method called when a column move needs to take place
    def OnColMove(self, evt):
        frm = evt.GetMoveColumn()       # Column being moved
        to = evt.GetBeforeColumn()      # Before which column to insert
        self.GetTable().MoveColumn(frm, to)

    # Event method called when a row move needs to take place
    def OnRowMove(self, evt):
        frm = evt.GetMoveRow()          # Row being moved
        to = evt.GetBeforeRow()         # Before which row to insert
        self.GetTable().MoveRow(frm, to)

    def RenameCol(self, col):
        label = self.GetTable().colLabels[col]
        dlg = wx.TextEntryDialog(
                self, 'New name for Column Title',
                'Rename', 'More')
        dlg.SetValue(label)
        if dlg.ShowModal() == wx.ID_OK:
            self.GetTable().RenameCol(col, dlg.GetValue())
        dlg.Destroy()

    def InsertCol(self, col):
        dlg = wx.TextEntryDialog(
                self, 'Name for new Column Title',
                'New', 'More')
        dlg.SetValue('NewTitle')
        if dlg.ShowModal() == wx.ID_OK:
            self.GetTable().InsertCol(col, dlg.GetValue())
        dlg.Destroy()


class MainFrame2(wx.Frame):
    def __init__(self, parent, log):
        wx.Frame.__init__(self, parent, -1,
                          "AMT Lite",
                          size=(640, 480))

        self.grid = DragableGrid(self, log)

        self.CreateStatusBar()
        self.SetStatusText("Welcome to AMT-Lite")

        # Prepare the menu bar
        menuBar = wx.MenuBar()

        # File
        file_menu = wx.Menu()
        load = file_menu.Append(
            wx.ID_ANY, "&Load", "Load an artifacts file.")
        save = file_menu.Append(
            wx.ID_ANY, "&Save", "Save the current artifacts file.")
        save_as = file_menu.Append(
            wx.ID_ANY, "&Save as",
            "Save the current artifacts to a specified file.")
        file_menu.AppendSeparator()
        close = file_menu.Append(wx.ID_ANY, "&Close", "Close this frame")
        menuBar.Append(file_menu, "&File")

        # View
        view_menu = wx.Menu()

        # View/Visibility
        visibility_menu = wx.Menu()
        unhide_cols = visibility_menu.Append(
            wx.ID_ANY, "Un-Hide All Columns")
        unhide_rows = visibility_menu.Append(
            wx.ID_ANY, "Un-Hide All Rows")
        unhide_all = visibility_menu.Append(
            wx.ID_ANY, "Un-Hide All")
        view_menu.AppendMenu(wx.ID_ANY, "Visibility", visibility_menu)
        menuBar.Append(view_menu, "&View")

        self.SetMenuBar(menuBar)

        # Menu events
        self.Bind(wx.EVT_MENU, self.Load, load)
        self.Bind(wx.EVT_MENU, self.Save, save)
        self.Bind(wx.EVT_MENU, self.SaveAs, save_as)
        self.Bind(wx.EVT_MENU, self.CloseWindow, close)
        self.Bind(wx.EVT_MENU, self.UnHideCols, unhide_cols)
        self.Bind(wx.EVT_MENU, self.UnHideRows, unhide_rows)
        self.Bind(wx.EVT_MENU, self.UnHideAll, unhide_all)

    def UnHideCols(self, event):
        self.grid.GetTable().UnHideCols()

    def UnHideRows(self, event):
        self.grid.GetTable().UnHideRows()

    def UnHideAll(self, event):
        self.grid.GetTable().UnHideAll()

    def Load(self, event):
        wildcard = "YAML File (*.yaml)|*.yaml|"     \
                   "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Select Artifacts File",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
            )

        # Show the dialog and retrieve the user response. If it is the OK
        # response, process the data.
        if dlg.ShowModal() == wx.ID_OK:
            self.grid.GetTable().Load(dlg.GetPath())
            for i, c in enumerate(self.grid.GetTable().col_properties):
                self.grid.SetColSize(i, c['Width'])
            self.SetTitle(os.path.basename(dlg.GetPath()))

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def Save(self, event):
        self.grid.GetTable().Save()

    def SaveAs(self, event):
        wildcard = "YAML File (*.yaml)|*.yaml|"     \
                   "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Select Artifacts File",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
            )

        # Show the dialog and retrieve the user response. If it is the OK
        # response, process the data.
        if dlg.ShowModal() == wx.ID_OK:
            self.grid.GetTable().SaveAs(dlg.GetPath())

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def CloseWindow(self, event):
        self.Close()


class MainFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(800, 600),
                 style=wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()

        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)

        # set frame icon
        # self.SetIcon(images.Mondrian.GetIcon())

        # set up default notebook style
        self._notebook_style = (aui.AUI_NB_DEFAULT_STYLE |
                                aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER)
        self._notebook_theme = 0

        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.log = log

        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText("Ready")

        self.BuildPanes()
        self.CreateMenuBar()
        self.BindEvents()

    def CreateMenuBar(self):

        # create menu
        mb = wx.MenuBar()

        # File Menu #
        file_menu = wx.Menu()

        # Load
        load = file_menu.Append(wx.ID_ANY, "Load")
        self.Bind(wx.EVT_MENU, self.OnLoad, load)

        # Save
        save = file_menu.Append(wx.ID_ANY, "Save")
        self.Bind(wx.EVT_MENU, self.OnSave, save)

        # Save As
        save_as = file_menu.Append(wx.ID_ANY, "Save As")
        self.Bind(wx.EVT_MENU, self.OnSaveAs, save_as)

        # Exit
        exit = file_menu.Append(wx.ID_ANY, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        view_menu = wx.Menu()
        view_menu.Append(ID_CreateText, "Create Text Control")
        view_menu.Append(ID_CreateHTML, "Create HTML Control")
        view_menu.Append(ID_CreateTree, "Create Tree")
        view_menu.Append(ID_CreateGrid, "Create Grid")
        view_menu.Append(ID_CreateNotebook, "Create Notebook")
        view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
        view_menu.AppendSeparator()
        view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
        view_menu.Append(ID_TextContent,
                         "Use a Text Control for the Content Pane")
        view_menu.Append(ID_HTMLContent,
                         "Use an HTML Control for the Content Pane")
        view_menu.Append(ID_TreeContent,
                         "Use a Tree Control for the Content Pane")
        view_menu.Append(ID_NotebookContent,
                         "Use a AuiNotebook control for the Content Pane")
        view_menu.Append(ID_SizeReportContent,
                         "Use a Size Reporter for the Content Pane")
        view_menu.AppendSeparator()

        options_menu = wx.Menu()
        options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
        options_menu.AppendRadioItem(
            ID_VenetianBlindsHint, "Venetian Blinds Hint")
        options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
        options_menu.AppendRadioItem(ID_NoHint, "No Hint")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
        options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
        options_menu.AppendCheckItem(
            ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
        options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
        options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
        options_menu.AppendCheckItem(ID_LiveUpdate, "Live Resize Update")
        options_menu.AppendCheckItem(
            ID_NativeMiniframes, "Use Native wx.MiniFrames")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(
            ID_MinimizePosSmart, "Minimize in Smart mode").Check()
        options_menu.AppendRadioItem(ID_MinimizePosTop, "Minimize on Top")
        options_menu.AppendRadioItem(
            ID_MinimizePosLeft, "Minimize on the Left")
        options_menu.AppendRadioItem(
            ID_MinimizePosRight, "Minimize on the Right")
        options_menu.AppendRadioItem(
            ID_MinimizePosBottom, "Minimize at the Bottom")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(
            ID_MinimizeCaptSmart, "Smart Minimized Caption")
        options_menu.AppendRadioItem(
            ID_MinimizeCaptHorz, "Horizontal Minimized Caption")
        options_menu.AppendRadioItem(
            ID_MinimizeCaptHide, "Hidden Minimized Caption").Check()
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(
            ID_AnimateFrames, "Animate Dock/Close/Minimize Of Floating Panes")
        options_menu.AppendCheckItem(
            ID_SmoothDocking, "Smooth Docking Effects (PyQT Style)")
        options_menu.AppendSeparator()
        options_menu.Append(
            ID_TransparentPane, "Set Floating Panes Transparency")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_DefaultDockArt, "Default DockArt")
        options_menu.AppendRadioItem(ID_ModernDockArt, "Modern Dock Art")
        options_menu.AppendSeparator()
        options_menu.Append(ID_SnapToScreen, "Snap To Screen")
        options_menu.AppendCheckItem(
            ID_SnapPanes, "Snap Panes To Managed Window")
        options_menu.AppendCheckItem(ID_FlyOut, "Use Fly-Out Floating Panes")
        options_menu.AppendSeparator()
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
        options_menu.AppendRadioItem(
            ID_VerticalGradient, "Vertical Caption Gradient")
        options_menu.AppendRadioItem(
            ID_HorizontalGradient, "Horizontal Caption Gradient")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(
            ID_PreviewMinimized, "Preview Minimized Panes")
        options_menu.AppendSeparator()
        options_menu.Append(ID_Settings, "Settings Pane")

        notebook_menu = wx.Menu()
        notebook_menu.AppendRadioItem(
            ID_NotebookArtGloss, "Glossy Theme (Default)")
        notebook_menu.AppendRadioItem(ID_NotebookArtSimple, "Simple Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC71, "VC71 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtFF2, "Firefox 2 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC8, "VC8 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtChrome, "Chrome Theme")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(
            ID_NotebookNoCloseButton, "No Close Button")
        notebook_menu.AppendRadioItem(
            ID_NotebookCloseButton, "Close Button At Right")
        notebook_menu.AppendRadioItem(
            ID_NotebookCloseButtonAll, "Close Button On All Tabs")
        notebook_menu.AppendRadioItem(
            ID_NotebookCloseButtonActive, "Close Button On Active Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(
            ID_NotebookCloseOnLeft, "Close Button On The Left Of Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookAlignTop, "Tab Top Alignment")
        notebook_menu.AppendRadioItem(
            ID_NotebookAlignBottom, "Tab Bottom Alignment")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(
            ID_NotebookAllowTabMove, "Allow Tab Move")
        notebook_menu.AppendCheckItem(
            ID_NotebookAllowTabExternalMove, "Allow External Tab Move")
        notebook_menu.AppendCheckItem(
            ID_NotebookAllowTabSplit, "Allow Notebook Split")
        notebook_menu.AppendCheckItem(
            ID_NotebookTabFloat, "Allow Single Tab Floating")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(
            ID_NotebookDclickUnsplit, "Unsplit On Sash Double-Click")
        notebook_menu.AppendCheckItem(
            ID_NotebookTabDrawDnd, "Draw Tab Image On Drag 'n' Drop")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(
            ID_NotebookScrollButtons, "Scroll Buttons Visible")
        notebook_menu.AppendCheckItem(
            ID_NotebookWindowList, "Window List Button Visible")
        notebook_menu.AppendCheckItem(
            ID_NotebookTabFixedWidth, "Fixed-Width Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(
            ID_NotebookHideSingle, "Hide On Single Tab")
        notebook_menu.AppendCheckItem(ID_NotebookSmartTab, "Use Smart Tabbing")
        notebook_menu.AppendCheckItem(
            ID_NotebookUseImagesDropDown, "Use Tab Images In Dropdown Menu")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(ID_NotebookMinMaxWidth, "Set Min/Max Tab Widths")
        notebook_menu.Append(
            ID_NotebookMultiLine, "Add A Multi-Line Label Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(
            ID_NotebookPreview, "Preview Of All Notebook Pages")

        perspectives_menu = wx.Menu()

        self._perspectives_menu = wx.Menu()
        self._perspectives_menu.Append(
            ID_CreatePerspective, "Create Perspective")
        self._perspectives_menu.Append(
            ID_CopyPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._perspectives_menu.AppendSeparator()
        self._perspectives_menu.Append(
            ID_FirstPerspective+0, "Default Startup")
        self._perspectives_menu.Append(ID_FirstPerspective+1, "All Panes")

        self._nb_perspectives_menu = wx.Menu()
        self._nb_perspectives_menu.Append(
            ID_CreateNBPerspective, "Create Perspective")
        self._nb_perspectives_menu.Append(
            ID_CopyNBPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._nb_perspectives_menu.AppendSeparator()
        self._nb_perspectives_menu.Append(
            ID_FirstNBPerspective + 0, "Default Startup")

        guides_menu = wx.Menu()
        guides_menu.AppendRadioItem(
            ID_StandardGuides, "Standard Docking Guides")
        guides_menu.AppendRadioItem(
            ID_AeroGuides, "Aero-Style Docking Guides")
        guides_menu.AppendRadioItem(
            ID_WhidbeyGuides, "Whidbey-Style Docking Guides")

        perspectives_menu.AppendMenu(
            wx.ID_ANY, "Frame Perspectives", self._perspectives_menu)
        perspectives_menu.AppendMenu(
            wx.ID_ANY, "AuiNotebook Perspectives", self._nb_perspectives_menu)
        perspectives_menu.AppendSeparator()
        perspectives_menu.AppendMenu(wx.ID_ANY, "Docking Guides", guides_menu)

        action_menu = wx.Menu()
        action_menu.AppendCheckItem(ID_VetoTree, "Veto Floating Of Tree Pane")
        action_menu.AppendCheckItem(ID_VetoText, "Veto Docking Of Fixed Pane")
        action_menu.AppendSeparator()

        attention_menu = wx.Menu()

        self._requestPanes = {}
        for indx, pane in enumerate(self._mgr.GetAllPanes()):
            if pane.IsToolbar():
                continue
            if not pane.caption or not pane.name:
                continue
            ids = wx.ID_HIGHEST + 12345 + indx
            self._requestPanes[ids] = pane.name
            attention_menu.Append(ids, pane.caption)

        action_menu.AppendMenu(
            wx.ID_ANY, "Request User Attention For", attention_menu)

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")

        mb.Append(file_menu, "&File")
        mb.Append(view_menu, "&View")
        mb.Append(perspectives_menu, "&Perspectives")
        mb.Append(options_menu, "&Options")
        mb.Append(notebook_menu, "&Notebook")
        mb.Append(action_menu, "&Actions")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)

    def BuildPanes(self):

        # min size for the frame itself isn't completely done.
        # see the end up AuiManager.Update() for the test
        # code. For now, just hard code a frame minimum size
        self.SetMinSize(wx.Size(400, 300))

        # add a bunch of panes
        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("AMT-Tree").Caption("Artifacts").
                          Left().Layer(1).Position(1).CloseButton(True).
                          MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().
                          Name("autonotebook").Caption("Console").
                          Bottom().Layer(1).Position(1).MinimizeButton(True))

        self._mgr.AddPane(SettingsPanel(self, self), aui.AuiPaneInfo().
                          Name("settings").Caption("Dock Manager Settings").
                          Dockable(False).Float().Hide().MinimizeButton(True))

        # create some center panes

        self._mgr.AddPane(self.CreateHTMLCtrl(),
                          aui.AuiPaneInfo().Name("html_content").
                          CenterPane().Hide().MinimizeButton(True))

        # "commit" all changes made to AuiManager
        self._mgr.Update()

    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MENU, self.OnCreateTree, id=ID_CreateTree)
        self.Bind(wx.EVT_MENU, self.OnCreateGrid, id=ID_CreateGrid)
        self.Bind(wx.EVT_MENU, self.OnCreateText, id=ID_CreateText)
        self.Bind(wx.EVT_MENU, self.OnCreateHTML, id=ID_CreateHTML)
        self.Bind(wx.EVT_MENU, self.OnCreateSizeReport, id=ID_CreateSizeReport)
        self.Bind(wx.EVT_MENU, self.OnCreateNotebook, id=ID_CreateNotebook)
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective,
                  id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyPerspectiveCode,
                  id=ID_CopyPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnCreateNBPerspective,
                  id=ID_CreateNBPerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyNBPerspectiveCode,
                  id=ID_CopyNBPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_StandardGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_AeroGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_WhidbeyGuides)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowFloating)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_RectangleHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_HintFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentDrag)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_LiveUpdate)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_SmoothDocking)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NativeMiniframes)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosTop)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosLeft)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosRight)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition,
                  id=ID_MinimizePosBottom)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHorz)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHide)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AnimateFrames)
        self.Bind(wx.EVT_MENU, self.OnTransparentPane, id=ID_TransparentPane)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_ModernDockArt)
        self.Bind(wx.EVT_MENU, self.OnSnapToScreen, id=ID_SnapToScreen)
        self.Bind(wx.EVT_MENU, self.OnSnapPanes, id=ID_SnapPanes)
        self.Bind(wx.EVT_MENU, self.OnFlyOut, id=ID_FlyOut)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowActivePane)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtGloss)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtSimple)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC71)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtFF2)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC8)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtChrome)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag,
                  id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseOnLeft)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignTop)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignBottom)
        self.Bind(wx.EVT_MENU, self.OnMinMaxTabWidth,
                  id=ID_NotebookMinMaxWidth)
        self.Bind(wx.EVT_MENU, self.OnPreview, id=ID_NotebookPreview)
        self.Bind(wx.EVT_MENU, self.OnAddMultiLine, id=ID_NotebookMultiLine)

        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_NoGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_VerticalGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_MENU, self.OnSettings, id=ID_Settings)
        self.Bind(wx.EVT_MENU, self.OnPreviewMinimized, id=ID_PreviewMinimized)
        self.Bind(wx.EVT_MENU, self.OnCustomizeToolbar, id=ID_CustomizeToolbar)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_GridContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TreeContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TextContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane,
                  id=ID_SizeReportContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_HTMLContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_NotebookContent)
        self.Bind(wx.EVT_MENU, self.OnVetoTree, id=ID_VetoTree)
        self.Bind(wx.EVT_MENU, self.OnVetoText, id=ID_VetoText)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_MENU, self.OnRequestUserAttention, id=ids)

        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective,
                  id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestoreNBPerspective,
                  id=ID_FirstNBPerspective,
                  id2=ID_FirstNBPerspective+1000)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AnimateFrames)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_FlyOut)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI,
                  id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoTree)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoText)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_StandardGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AeroGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_WhidbeyGuides)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ids)

        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem,
                  id=ID_DropDownToolbarItem)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(aui.EVT_AUINOTEBOOK_ALLOW_DND, self.OnAllowNotebookDnD)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnNotebookPageClose)

        self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnFloatDock)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnFloatDock)

        self.timer = wx.Timer(self)
        self.timer.Start(100)

    def __del__(self):

        self.timer.Stop()

    def GetDockArt(self):

        return self._mgr.GetArtProvider()

    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()

    def OnEraseBackground(self, event):

        event.Skip()

    def OnSize(self, event):

        event.Skip()

    def OnSettings(self, event):

        # show the settings pane, and float it
        floating_pane = self._mgr.GetPane("settings").Float().Show()

        if floating_pane.floating_pos == wx.DefaultPosition:
            floating_pane.FloatingPosition(self.GetStartPosition())

        self._mgr.Update()

    def OnPreviewMinimized(self, event):

        agwFlags = self._mgr.GetAGWFlags()

        if event.IsChecked():
            agwFlags ^= aui.AUI_MGR_PREVIEW_MINIMIZED_PANES
        else:
            agwFlags &= ~aui.AUI_MGR_PREVIEW_MINIMIZED_PANES

        self._mgr.SetAGWFlags(agwFlags)

    def OnTransparentPane(self, event):

        dlg = wx.TextEntryDialog(
            self, "Enter a transparency value (0-255):", "Pane transparency")

        dlg.SetValue("%d" % self._transparency)
        if dlg.ShowModal() != wx.ID_OK:
            return

        transparency = int(dlg.GetValue())
        dlg.Destroy()
        try:
            transparency = int(transparency)
        except:
            dlg = wx.MessageDialog(
                self, 'Invalid transparency value. Transparency'
                      ' should be an integer between 0 and 255.',
                'Error',
                wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if transparency < 0 or transparency > 255:
            dlg = wx.MessageDialog(
                self, 'Invalid transparency value. Transparency'
                      ' should be an integer between 0 and 255.',
                'Error',
                wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        self._transparency = transparency
        panes = self._mgr.GetAllPanes()
        for pane in panes:
            pane.Transparent(self._transparency)

        self._mgr.Update()

    def OnDockArt(self, event):

        if event.GetId() == ID_DefaultDockArt:
            self._mgr.SetArtProvider(aui.AuiDefaultDockArt())
        else:
            if self._mgr.CanUseModernDockArt():
                self._mgr.SetArtProvider(aui.ModernDockArt(self))

        self._mgr.Update()
        self.Refresh()

    def OnSnapToScreen(self, event):

        self._mgr.SnapToScreen(True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP)

    def OnSnapPanes(self, event):

        allPanes = self._mgr.GetAllPanes()

        if not self._snapped:
            self._captions = {}
            for pane in allPanes:
                self._captions[pane.name] = pane.caption

        toSnap = not self._snapped

        if toSnap:
            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window,
                                                  aui.AuiNotebook):
                    continue

                snap = random.randint(0, 4)
                if snap == 0:
                    # Snap everywhere
                    pane.Caption(pane.caption + " (Snap Everywhere)")
                    pane.Snappable(True)
                elif snap == 1:
                    # Snap left
                    pane.Caption(pane.caption + " (Snap Left)")
                    pane.LeftSnappable(True)
                elif snap == 2:
                    # Snap right
                    pane.Caption(pane.caption + " (Snap Right)")
                    pane.RightSnappable(True)
                elif snap == 3:
                    # Snap top
                    pane.Caption(pane.caption + " (Snap Top)")
                    pane.TopSnappable(True)
                elif snap == 4:
                    # Snap bottom
                    pane.Caption(pane.caption + " (Snap Bottom)")
                    pane.BottomSnappable(True)

        else:

            for pane in allPanes:
                if pane.IsToolbar() or isinstance(
                        pane.window, aui.AuiNotebook):
                    continue

                pane.Caption(self._captions[pane.name])
                pane.Snappable(False)

        self._snapped = toSnap
        self._mgr.Update()
        self.Refresh()

    def OnFlyOut(self, event):

        checked = event.IsChecked()
        pane = self._mgr.GetPane("test8")

        if checked:
            dlg = wx.MessageDialog(self, 'The tree pane will have fly-out'
                                   ' behaviour when floating.',
                                   'Message',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pane.FlyOut(True)
        else:
            pane.FlyOut(False)

        self._mgr.Update()

    def OnCustomizeToolbar(self, event):

        wx.MessageBox("Customize Toolbar clicked", "AMT Test")

    def OnGradient(self, event):

        evId = event.GetId()
        if evId == ID_NoGradient:
            gradient = aui.AUI_GRADIENT_NONE
        elif evId == ID_VerticalGradient:
            gradient = aui.AUI_GRADIENT_VERTICAL
        elif evId == ID_HorizontalGradient:
            gradient = aui.AUI_GRADIENT_HORIZONTAL

        self._mgr.GetArtProvider().SetMetric(
            aui.AUI_DOCKART_GRADIENT_TYPE, gradient)
        self._mgr.Update()

    def OnManagerFlag(self, event):

        flag = 0
        evId = event.GetId()

        if evId in [ID_TransparentHint, ID_VenetianBlindsHint,
                    ID_RectangleHint, ID_NoHint]:

            agwFlags = self._mgr.GetAGWFlags()
            agwFlags &= ~aui.AUI_MGR_TRANSPARENT_HINT
            agwFlags &= ~aui.AUI_MGR_VENETIAN_BLINDS_HINT
            agwFlags &= ~aui.AUI_MGR_RECTANGLE_HINT
            self._mgr.SetAGWFlags(agwFlags)

        if evId == ID_AllowFloating:
            flag = aui.AUI_MGR_ALLOW_FLOATING
        elif evId == ID_TransparentDrag:
            flag = aui.AUI_MGR_TRANSPARENT_DRAG
        elif evId == ID_HintFade:
            flag = aui.AUI_MGR_HINT_FADE
        elif evId == ID_NoVenetianFade:
            flag = aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE
        elif evId == ID_AllowActivePane:
            flag = aui.AUI_MGR_ALLOW_ACTIVE_PANE
        elif evId == ID_TransparentHint:
            flag = aui.AUI_MGR_TRANSPARENT_HINT
        elif evId == ID_VenetianBlindsHint:
            flag = aui.AUI_MGR_VENETIAN_BLINDS_HINT
        elif evId == ID_RectangleHint:
            flag = aui.AUI_MGR_RECTANGLE_HINT
        elif evId == ID_LiveUpdate:
            flag = aui.AUI_MGR_LIVE_RESIZE
        elif evId == ID_AnimateFrames:
            flag = aui.AUI_MGR_ANIMATE_FRAMES
        elif evId == ID_SmoothDocking:
            flag = aui.AUI_MGR_SMOOTH_DOCKING
        elif evId == ID_NativeMiniframes:
            flag = aui.AUI_MGR_USE_NATIVE_MINIFRAMES

        if flag:
            self._mgr.SetAGWFlags(self._mgr.GetAGWFlags() ^ flag)

        self._mgr.Update()

    def OnMinimizePosition(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizePosSmart:
            minize_mode |= aui.AUI_MINIMIZE_POS_SMART
        elif evId == ID_MinimizePosTop:
            minize_mode |= aui.AUI_MINIMIZE_POS_TOP
        elif evId == ID_MinimizePosLeft:
            minize_mode |= aui.AUI_MINIMIZE_POS_LEFT
        elif evId == ID_MinimizePosRight:
            minize_mode |= aui.AUI_MINIMIZE_POS_RIGHT
        elif evId == ID_MinimizePosBottom:
            minize_mode |= aui.AUI_MINIMIZE_POS_BOTTOM

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            pane.MinimizeMode(minize_mode |
                              (pane.GetMinimizeMode() &
                               aui.AUI_MINIMIZE_CAPT_MASK))

    def OnMinimizeCaption(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizeCaptSmart:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_SMART
        elif evId == ID_MinimizeCaptHorz:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HORZ
        elif evId == ID_MinimizeCaptHide:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HIDE

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            pane.MinimizeMode(minize_mode |
                              (pane.GetMinimizeMode() &
                               aui.AUI_MINIMIZE_POS_MASK))

    def OnNotebookFlag(self, event):

        evId = event.GetId()

        if evId in [ID_NotebookNoCloseButton, ID_NotebookCloseButton,
                    ID_NotebookCloseButtonAll, ID_NotebookCloseButtonActive]:

            self._notebook_style &= ~(aui.AUI_NB_CLOSE_BUTTON |
                                      aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                      aui.AUI_NB_CLOSE_ON_ALL_TABS)

            if evId == ID_NotebookCloseButton:
                self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON
            elif evId == ID_NotebookCloseButtonAll:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS
            elif evId == ID_NotebookCloseButtonActive:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

        if evId == ID_NotebookAllowTabMove:
            self._notebook_style ^= aui.AUI_NB_TAB_MOVE

        if evId == ID_NotebookAllowTabExternalMove:
            self._notebook_style ^= aui.AUI_NB_TAB_EXTERNAL_MOVE

        elif evId == ID_NotebookAllowTabSplit:
            self._notebook_style ^= aui.AUI_NB_TAB_SPLIT

        elif evId == ID_NotebookTabFloat:
            self._notebook_style ^= aui.AUI_NB_TAB_FLOAT

        elif evId == ID_NotebookTabDrawDnd:
            self._notebook_style ^= aui.AUI_NB_DRAW_DND_TAB

        elif evId == ID_NotebookWindowList:
            self._notebook_style ^= aui.AUI_NB_WINDOWLIST_BUTTON

        elif evId == ID_NotebookScrollButtons:
            self._notebook_style ^= aui.AUI_NB_SCROLL_BUTTONS

        elif evId == ID_NotebookTabFixedWidth:
            self._notebook_style ^= aui.AUI_NB_TAB_FIXED_WIDTH

        elif evId == ID_NotebookHideSingle:
            self._notebook_style ^= aui.AUI_NB_HIDE_ON_SINGLE_TAB

        elif evId == ID_NotebookSmartTab:
            self._notebook_style ^= aui.AUI_NB_SMART_TABS

        elif evId == ID_NotebookUseImagesDropDown:
            self._notebook_style ^= aui.AUI_NB_USE_IMAGES_DROPDOWN

        elif evId == ID_NotebookCloseOnLeft:
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_TAB_LEFT

        all_panes = self._mgr.GetAllPanes()

        for pane in all_panes:

            if isinstance(pane.window, aui.AuiNotebook):
                nb = pane.window

                if evId == ID_NotebookArtGloss:

                    nb.SetArtProvider(aui.AuiDefaultTabArt())
                    self._notebook_theme = 0

                elif evId == ID_NotebookArtSimple:
                    nb.SetArtProvider(aui.AuiSimpleTabArt())
                    self._notebook_theme = 1

                elif evId == ID_NotebookArtVC71:
                    nb.SetArtProvider(aui.VC71TabArt())
                    self._notebook_theme = 2

                elif evId == ID_NotebookArtFF2:
                    nb.SetArtProvider(aui.FF2TabArt())
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8:
                    nb.SetArtProvider(aui.VC8TabArt())
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome:
                    nb.SetArtProvider(aui.ChromeTabArt())
                    self._notebook_theme = 5

                if nb.GetAGWWindowStyleFlag() & aui.AUI_NB_BOTTOM == 0:
                    nb.SetAGWWindowStyleFlag(self._notebook_style)

                if evId == ID_NotebookCloseButtonAll:
                    # Demonstrate how to remove a close button from a tab
                    nb.SetCloseButton(2, False)
                elif evId == ID_NotebookDclickUnsplit:
                    nb.SetSashDClickUnsplit(event.IsChecked())

                nb.Refresh()
                nb.Update()

    def OnUpdateUI(self, event):

        agwFlags = self._mgr.GetAGWFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(
                aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)

        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(
                aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)

        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(
                aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)

        elif evId == ID_AllowFloating:
            event.Check((agwFlags & aui.AUI_MGR_ALLOW_FLOATING) != 0)

        elif evId == ID_TransparentDrag:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)

        elif evId == ID_TransparentHint:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)

        elif evId == ID_LiveUpdate:
            event.Check(aui.AuiManager_HasLiveResize(self._mgr))

        elif evId == ID_VenetianBlindsHint:
            event.Check((agwFlags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)

        elif evId == ID_RectangleHint:
            event.Check((agwFlags & aui.AUI_MGR_RECTANGLE_HINT) != 0)

        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                          aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                          aui.AUI_MGR_RECTANGLE_HINT) & agwFlags) == 0)

        elif evId == ID_HintFade:
            event.Check((agwFlags & aui.AUI_MGR_HINT_FADE) != 0)

        elif evId == ID_NoVenetianFade:
            event.Check((agwFlags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)

        elif evId == ID_NativeMiniframes:
            event.Check(aui.AuiManager_UseNativeMiniframes(self._mgr))

        elif evId == ID_SmoothDocking:
            event.Check((agwFlags & aui.AUI_MGR_SMOOTH_DOCKING) != 0)

        elif evId == ID_AnimateFrames:
            event.Check((agwFlags & aui.AUI_MGR_ANIMATE_FRAMES) != 0)

        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(
                self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(
                self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)

        elif evId == ID_FlyOut:
            pane = self._mgr.GetPane("test8")
            event.Check(pane.IsFlyOut())

        elif evId == ID_AeroGuides:
            event.Check(agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES != 0)

        elif evId == ID_WhidbeyGuides:
            event.Check(agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES != 0)

        elif evId == ID_StandardGuides:
            event.Check((
                agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES == 0) and
                (agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES == 0))

        elif evId == ID_PreviewMinimized:
            event.Check(agwFlags & aui.AUI_MGR_PREVIEW_MINIMIZED_PANES)

        elif evId == ID_NotebookNoCloseButton:
            event.Check((
                self._notebook_style & (aui.AUI_NB_CLOSE_BUTTON |
                                        aui.AUI_NB_CLOSE_ON_ALL_TABS |
                                        aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)) != 0)

        elif evId == ID_NotebookCloseButton:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_BUTTON) != 0)

        elif evId == ID_NotebookCloseButtonAll:
            event.Check((
                self._notebook_style & aui.AUI_NB_CLOSE_ON_ALL_TABS) != 0)

        elif evId == ID_NotebookCloseButtonActive:
            event.Check((
                self._notebook_style & aui.AUI_NB_CLOSE_ON_ACTIVE_TAB) != 0)

        elif evId == ID_NotebookAllowTabSplit:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_SPLIT) != 0)

        elif evId == ID_NotebookTabFloat:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FLOAT) != 0)

        elif evId == ID_NotebookTabDrawDnd:
            event.Check((self._notebook_style & aui.AUI_NB_DRAW_DND_TAB) != 0)

        elif evId == ID_NotebookAllowTabMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_MOVE) != 0)

        elif evId == ID_NotebookAllowTabExternalMove:
            event.Check((
                self._notebook_style & aui.AUI_NB_TAB_EXTERNAL_MOVE) != 0)

        elif evId == ID_NotebookScrollButtons:
            event.Check((
                self._notebook_style & aui.AUI_NB_SCROLL_BUTTONS) != 0)

        elif evId == ID_NotebookWindowList:
            event.Check((
                self._notebook_style & aui.AUI_NB_WINDOWLIST_BUTTON) != 0)

        elif evId == ID_NotebookTabFixedWidth:
            event.Check((
                self._notebook_style & aui.AUI_NB_TAB_FIXED_WIDTH) != 0)

        elif evId == ID_NotebookHideSingle:
            event.Check((
                self._notebook_style & aui.AUI_NB_HIDE_ON_SINGLE_TAB) != 0)

        elif evId == ID_NotebookSmartTab:
            event.Check((self._notebook_style & aui.AUI_NB_SMART_TABS) != 0)

        elif evId == ID_NotebookUseImagesDropDown:
            event.Check((
                self._notebook_style & aui.AUI_NB_USE_IMAGES_DROPDOWN) != 0)

        elif evId == ID_NotebookCloseOnLeft:
            event.Check((
                self._notebook_style & aui.AUI_NB_CLOSE_ON_TAB_LEFT) != 0)

        elif evId == ID_NotebookArtGloss:
            event.Check(self._notebook_theme == 0)

        elif evId == ID_NotebookArtSimple:
            event.Check(self._notebook_theme == 1)

        elif evId == ID_NotebookArtVC71:
            event.Check(self._notebook_theme == 2)

        elif evId == ID_NotebookArtFF2:
            event.Check(self._notebook_theme == 3)

        elif evId == ID_NotebookArtVC8:
            event.Check(self._notebook_theme == 4)

        elif evId == ID_NotebookArtChrome:
            event.Check(self._notebook_theme == 5)

        elif evId == ID_VetoTree:
            event.Check(self._veto_tree)

        elif evId == ID_VetoText:
            event.Check(self._veto_text)

        else:
            for ids in self._requestPanes:
                if evId == ids:
                    paneName = self._requestPanes[ids]
                    pane = self._mgr.GetPane(paneName)
                    event.Enable(pane.IsShown())

    def OnPaneClose(self, event):

        if event.pane.name == "test10":

            msg = "Are you sure you want to "
            if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
                msg += "minimize "
            else:
                msg += "close/hide "

            res = wx.MessageBox(msg + "this pane?", "AMT", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()

    def OnCreatePerspective(self, event):

        dlg = wx.TextEntryDialog(
            self, "Enter a name for the new perspective:", "AMT Test")

        dlg.SetValue("Perspective %u" % (len(self._perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._perspectives) == 0:
            self._perspectives_menu.AppendSeparator()

        self._perspectives_menu.Append(ID_FirstPerspective + len(
            self._perspectives), dlg.GetValue())
        self._perspectives.append(self._mgr.SavePerspective())

    def OnCopyPerspectiveCode(self, event):

        s = self._mgr.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()

    def OnRestorePerspective(self, event):

        self._mgr.LoadPerspective(
            self._perspectives[event.GetId() - ID_FirstPerspective])

    def OnCreateNBPerspective(self, event):

        dlg = wx.TextEntryDialog(
            self, "Enter a name for the new perspective:", "AMT Test")

        dlg.SetValue("Perspective %u" % (len(self._nb_perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._nb_perspectives) == 0:
            self._nb_perspectives_menu.AppendSeparator()

        auibook = self._mgr.GetPane("notebook_content").window
        self._nb_perspectives_menu.Append(
            ID_FirstNBPerspective + len(self._nb_perspectives), dlg.GetValue())
        self._nb_perspectives.append(auibook.SavePerspective())

    def OnCopyNBPerspectiveCode(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        s = auibook.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()

    def OnRestoreNBPerspective(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.LoadPerspective(self._nb_perspectives[event.GetId() -
                                                      ID_FirstNBPerspective])

    def OnGuides(self, event):

        useAero = event.GetId() == ID_AeroGuides
        useWhidbey = event.GetId() == ID_WhidbeyGuides
        agwFlags = self._mgr.GetAGWFlags()

        if useAero:
            agwFlags ^= aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
        elif useWhidbey:
            agwFlags ^= aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
        else:
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES

        self._mgr.SetAGWFlags(agwFlags)

    def OnNotebookPageClose(self, event):

        ctrl = event.GetEventObject()
        if isinstance(ctrl.GetPage(event.GetSelection()), wx.html.HtmlWindow):

            res = wx.MessageBox(
                "Are you sure you want to close/hide this notebook page?",
                "AMT", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()

    def OnAllowNotebookDnD(self, event):

        # for the purpose of this test application, explicitly
        # allow all noteboko drag and drop events
        event.Allow()

    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)

    def OnCreateTree(self, event):

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Caption("Tree Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        self._mgr.Update()

    def OnCreateGrid(self, event):

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().
                          Caption("Grid").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()

    def OnCreateHTML(self, event):

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().
                          Caption("HTML Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()

    def OnCreateNotebook(self, event):

        self._mgr.AddPane(
            self.CreateNotebook(), aui.AuiPaneInfo().
            Caption("Notebook").
            Float().FloatingPosition(self.GetStartPosition()).
            CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()

    def OnCreateText(self, event):

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().
                          Caption("Text Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          MinimizeButton(True))
        self._mgr.Update()

    def OnCreateSizeReport(self, event):

        self._mgr.AddPane(
            self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
            Caption("Client Size Reporter").
            Float().FloatingPosition(self.GetStartPosition()).
            CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()

    def OnChangeContentPane(self, event):

        self._mgr.GetPane("grid_content").Show(event.GetId() == ID_GridContent)
        self._mgr.GetPane("text_content").Show(event.GetId() == ID_TextContent)
        self._mgr.GetPane("tree_content").Show(event.GetId() == ID_TreeContent)
        self._mgr.GetPane("sizereport_content").Show(
            event.GetId() == ID_SizeReportContent)
        self._mgr.GetPane("html_content").Show(event.GetId() == ID_HTMLContent)
        self._mgr.GetPane("notebook_content").Show(
            event.GetId() == ID_NotebookContent)
        self._mgr.Update()

    def OnVetoTree(self, event):

        self._veto_tree = event.IsChecked()

    def OnVetoText(self, event):

        self._veto_text = event.IsChecked()

    def OnRequestUserAttention(self, event):

        ids = event.GetId()
        if ids not in self._requestPanes:
            return

        paneName = self._requestPanes[ids]
        pane = self._mgr.GetPane(paneName)
        self._mgr.RequestUserAttention(pane.window)

    def OnDropDownToolbarItem(self, event):

        if event.IsDropDownClicked():

            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = wx.Menu()
            bmp = wx.ArtProvider.GetBitmap(
                wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))

            m1 = wx.MenuItem(menuPopup, 10001, "Drop Down Item 1")
            m1.SetBitmap(bmp)
            menuPopup.AppendItem(m1)

            m2 = wx.MenuItem(menuPopup, 10002, "Drop Down Item 2")
            m2.SetBitmap(bmp)
            menuPopup.AppendItem(m2)

            m3 = wx.MenuItem(menuPopup, 10003, "Drop Down Item 3")
            m3.SetBitmap(bmp)
            menuPopup.AppendItem(m3)

            m4 = wx.MenuItem(menuPopup, 10004, "Drop Down Item 4")
            m4.SetBitmap(bmp)
            menuPopup.AppendItem(m4)

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)

    def OnTabAlignment(self, event):

        for pane in self._mgr.GetAllPanes():

            if isinstance(pane.window, aui.AuiNotebook):

                nb = pane.window
                style = nb.GetAGWWindowStyleFlag()

                if event.GetId() == ID_NotebookAlignTop:
                    style &= ~aui.AUI_NB_BOTTOM
                    style ^= aui.AUI_NB_TOP
                    nb.SetAGWWindowStyleFlag(style)
                elif event.GetId() == ID_NotebookAlignBottom:
                    style &= ~aui.AUI_NB_TOP
                    style ^= aui.AUI_NB_BOTTOM
                    nb.SetAGWWindowStyleFlag(style)

                self._notebook_style = style
                nb.Update()
                nb.Refresh()

    def OnMinMaxTabWidth(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        minTabWidth, maxTabWidth = auibook.GetMinMaxTabWidth()

        dlg = wx.TextEntryDialog(
            self, "Enter the minimum and maximum tab widths, separated by "
                  "a comma: AuiNotebook Tab Widths")

        dlg.SetValue("%d,%d" % (minTabWidth, maxTabWidth))
        if dlg.ShowModal() != wx.ID_OK:
            return

        value = dlg.GetValue()
        dlg.Destroy()

        try:
            minTabWidth, maxTabWidth = value.split(",")
            minTabWidth, maxTabWidth = int(minTabWidth), int(maxTabWidth)
        except:
            dlg = wx.MessageDialog(
                self, 'Invalid minimum/maximum tab width. Tab widths should '
                      'be 2 integers separated by a comma.',
                'Error',
                wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if minTabWidth > maxTabWidth:
            dlg = wx.MessageDialog(
                self, 'Invalid minimum/maximum tab width. Minimum tab width'
                      ' should be less of equal than maximum tab width.',
                'Error',
                wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        auibook.SetMinMaxTabWidth(minTabWidth, maxTabWidth)
        auibook.Refresh()
        auibook.Update()

    def OnPreview(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.NotebookPreview()

    def OnAddMultiLine(self, event):

        auibook = self._mgr.GetPane("notebook_content").window

        auibook.InsertPage(1, wx.TextCtrl(
            auibook, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
            wx.TE_MULTILINE | wx.NO_BORDER), "Multi-Line\nTab Labels", True)

        auibook.SetPageTextColour(1, wx.BLUE)

    def OnFloatDock(self, event):

        paneLabel = event.pane.caption
        etype = event.GetEventType()

        strs = "Pane %s " % paneLabel
        if etype == aui.wxEVT_AUI_PANE_FLOATING:
            strs += "is about to be floated"

            if event.pane.name == "test8" and self._veto_tree:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_FLOATED:
            strs += "has been floated"
        elif etype == aui.wxEVT_AUI_PANE_DOCKING:
            strs += "is about to be docked"

            if event.pane.name == "test11" and self._veto_text:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_DOCKED:
            strs += "has been docked"

        self.log.write(strs + "\n")

    def OnLoad(self, event):
        pass

    def OnSave(self, event):
        pass

    def OnSaveAs(self, event):
        pass

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):

        msg = "Artifact Management Tool v1.0.0.\n\n" + \
              "Author: Kenneth E. Bellock\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n"

        dlg = wx.MessageDialog(self, msg, "AMT",
                               wx.OK | wx.ICON_INFORMATION)

        if wx.Platform != '__WXMAC__':
            dlg.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL, False))

        dlg.ShowModal()
        dlg.Destroy()

    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = ""
            self._textCount += 1

        return wx.TextCtrl(self, -1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)

    def CreateGrid(self):

        grid = wx.grid.Grid(self, -1, wx.Point(0, 0), wx.Size(150, 250),
                            wx.NO_BORDER | wx.WANTS_CHARS)
        grid.CreateGrid(50, 20)
        return grid

    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(
            wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(
            wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AMT Project", 0)
        items = []

        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for item in items:
            tree.AppendItem(item, "Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)

        tree.Expand(root)

        return tree

    def CreateSizeReportCtrl(self, width=80, height=80):

        ctrl = SizeReportCtrl(
            self, -1, wx.DefaultPosition, wx.Size(width, height), self._mgr)
        return ctrl

    def CreateHTMLCtrl(self, parent=None):

        if not parent:
            parent = self

        ctrl = wx.html.HtmlWindow(
            parent, -1, wx.DefaultPosition, wx.Size(400, 300))
        ctrl.SetPage(GetIntroText())
        return ctrl

    def CreateNotebook(self):

        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(
            self, -1, wx.Point(client_size.x, client_size.y),
            wx.Size(430, 200), agwStyle=self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt,
                aui.FF2TabArt, aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(
            wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        ctrl.AddPage(self.CreateHTMLCtrl(
            ctrl), "Welcome to AMT", False, page_bmp)

        return ctrl

    def OnSwitchPane(self, event):

        items = ASD.SwitcherItems()
        items.SetRowCount(12)

        # Add the main windows and toolbars, in two separate columns We'll use
        # the item 'id' to store the notebook selection, or -1 if not a page

        for k in xrange(2):
            if k == 0:
                items.AddGroup(wx.GetTranslation("Main Windows"),
                               "mainwindows")
            else:
                items.AddGroup(wx.GetTranslation(
                    "Toolbars"), "toolbars").BreakColumn()

            for pane in self._mgr.GetAllPanes():
                name = pane.name
                caption = pane.caption
                if not caption:
                    continue

                toolBar = isinstance(pane.window, wx.ToolBar) or isinstance(
                    pane.window, aui.AuiToolBar)
                bitmap = (pane.icon.IsOk() and [pane.icon] or [
                    wx.NullBitmap])[0]

                if (toolBar and k == 1) or (not toolBar and k == 0):
                    items.AddItem(caption, name, -1, bitmap).SetWindow(
                        pane.window)

        # Now add the wxAuiNotebook pages
        items.AddGroup(wx.GetTranslation(
            "Notebook Pages"), "pages").BreakColumn()

        for pane in self._mgr.GetAllPanes():
            nb = pane.window
            if isinstance(nb, aui.AuiNotebook):
                for j in xrange(nb.GetPageCount()):

                    name = nb.GetPageText(j)
                    win = nb.GetPage(j)

                    items.AddItem(name, name, j,
                                  nb.GetPageBitmap(j)).SetWindow(win)

        # Select the focused window

        idx = items.GetIndexForFocus()
        if idx != wx.NOT_FOUND:
            items.SetSelection(idx)

        if wx.Platform == "__WXMAC__":
            items.SetBackgroundColour(wx.WHITE)

        # Show the switcher dialog

        dlg = ASD.SwitcherDialog(items, self, self._mgr)

        # In GTK+ we can't use Ctrl+Tab; we use Ctrl+/ instead and tell the
        # switcher to treat / in the same was as tab (i.e. cycle through the
        # names)

        if wx.Platform == "__WXGTK__":
            dlg.SetExtraNavigationKey('/')

        if wx.Platform == "__WXMAC__":
            dlg.SetBackgroundColour(wx.WHITE)
            dlg.SetModifierKey(wx.WXK_ALT)

        ans = dlg.ShowModal()

        if ans == wx.ID_OK and dlg.GetSelection() != -1:
            item = items.GetItem(dlg.GetSelection())

            if item.GetId() == -1:
                info = self._mgr.GetPane(item.GetName())
                info.Show()
                self._mgr.Update()
                info.window.SetFocus()

            else:
                nb = item.GetWindow().GetParent()
                win = item.GetWindow()
                if isinstance(nb, aui.AuiNotebook):
                    nb.SetSelection(item.GetId())
                    win.SetFocus()


def GetIntroText():

    text = (
        "<html><body>"
        "<h3>Welcome to AMT</h3>"
        "<br/><b>Overview</b><br/>"
        "<p>AMT is an artifact management tool. <\p>"
        "</body></html>")

    return text


def gui():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

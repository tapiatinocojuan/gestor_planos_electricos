# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 957,797 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter3 = wx.SplitterWindow( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )

		self.m_panel3 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter31 = wx.SplitterWindow( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter31.Bind( wx.EVT_IDLE, self.m_splitter31OnIdle )

		self.m_panel5 = wx.Panel( self.m_splitter31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer12.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dataViewListCtrl = wx.dataview.DataViewListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_dataViewListCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer12 )
		self.m_panel5.Layout()
		bSizer12.Fit( self.m_panel5 )
		self.m_panel6 = wx.Panel( self.m_splitter31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_carga = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl_carga, 1, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel6, wx.ID_ANY, u"Calc Carga", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_distancia = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_textCtrl_distancia, 1, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_panel6, wx.ID_ANY, u"Calc Distancias", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_button21, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer141, 0, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"No mezclar circuitos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		gSizer2.Add( self.m_checkBox2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"No unir placas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		gSizer2.Add( self.m_checkBox1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox3 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Calcular Alimentadores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		gSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Calcular controles", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True)
		gSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )


		bSizer13.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self.m_panel6, wx.ID_ANY, u"Calcular centro carga", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Buscar tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self.m_panel6, wx.ID_ANY, u"Buscar Espacios", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self.m_panel6, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer13.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer13 )
		self.m_panel6.Layout()
		bSizer13.Fit( self.m_panel6 )
		self.m_splitter31.SplitHorizontally( self.m_panel5, self.m_panel6, 165 )
		bSizer18.Add( self.m_splitter31, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer18 )
		self.m_panel3.Layout()
		bSizer18.Fit( self.m_panel3 )
		self.m_panel4 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter4 = wx.SplitterWindow( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )

		self.m_panel7 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer191 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl = wx.TreeCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer191.Add( self.m_treeCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer191 )
		self.m_panel7.Layout()
		bSizer191.Fit( self.m_panel7 )
		self.m_panel8 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter5 = wx.SplitterWindow( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter5.Bind( wx.EVT_IDLE, self.m_splitter5OnIdle )

		self.m_panel9 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter6 = wx.SplitterWindow( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter6.Bind( wx.EVT_IDLE, self.m_splitter6OnIdle )

		self.m_panel11 = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer221 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl_tags = wx.TreeCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer221.Add( self.m_treeCtrl_tags, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer221 )
		self.m_panel11.Layout()
		bSizer221.Fit( self.m_panel11 )
		self.m_panel12 = wx.Panel( self.m_splitter6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl_ramas = wx.TreeCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer23.Add( self.m_treeCtrl_ramas, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel12.SetSizer( bSizer23 )
		self.m_panel12.Layout()
		bSizer23.Fit( self.m_panel12 )
		self.m_splitter6.SplitVertically( self.m_panel11, self.m_panel12, 0 )
		bSizer21.Add( self.m_splitter6, 1, wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer21 )
		self.m_panel9.Layout()
		bSizer21.Fit( self.m_panel9 )
		self.m_panel10 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 0, 2 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.AutoSizeColumns()
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelValue( 0, u"Espacio" )
		self.m_grid1.SetColLabelValue( 1, u"Circuito" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer22 )
		self.m_panel10.Layout()
		bSizer22.Fit( self.m_panel10 )
		self.m_splitter5.SplitHorizontally( self.m_panel9, self.m_panel10, 208 )
		bSizer20.Add( self.m_splitter5, 1, wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer20 )
		self.m_panel8.Layout()
		bSizer20.Fit( self.m_panel8 )
		self.m_splitter4.SplitVertically( self.m_panel7, self.m_panel8, 0 )
		bSizer19.Add( self.m_splitter4, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer19 )
		self.m_panel4.Layout()
		bSizer19.Fit( self.m_panel4 )
		self.m_splitter3.SplitHorizontally( self.m_panel3, self.m_panel4, 337 )
		bSizer2.Add( self.m_splitter3, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel2, 0 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool5 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/importar.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar2.Realize()


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.on_change_size )
		self.m_splitter1.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.on_sash_changed )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_change )
		self.m_dataViewListCtrl.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.on_edit_data, id = wx.ID_ANY )
		self.m_button2.Bind( wx.EVT_BUTTON, self.on_calc_carga )
		self.m_button21.Bind( wx.EVT_BUTTON, self.on_calc_distancias_minimas )
		self.m_button3.Bind( wx.EVT_BUTTON, self.on_calc_centro_carga )
		self.m_button5.Bind( wx.EVT_BUTTON, self.on_buscar_tags )
		self.m_button6.Bind( wx.EVT_BUTTON, self.on_buscar_espacios )
		self.m_button8.Bind( wx.EVT_BUTTON, self.on_calcular_controles )
		self.m_treeCtrl.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.on_context_menu_treectrl )
		self.m_treeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click )
		self.m_treeCtrl_tags.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click_tags )
		self.m_treeCtrl_ramas.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click_ramas )
		self.m_panel2.Bind( wx.EVT_LEFT_DOWN, self.on_left_down )
		self.m_panel2.Bind( wx.EVT_MOTION, self.on_mouse_motion )
		self.m_panel2.Bind( wx.EVT_PAINT, self.on_paint )
		self.m_panel2.Bind( wx.EVT_RIGHT_DOWN, self.on_context_menu )
		self.Bind( wx.EVT_TOOL, self.on_save, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_open, id = self.m_tool6.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_change_size( self, event ):
		event.Skip()

	def on_sash_changed( self, event ):
		event.Skip()

	def on_file_change( self, event ):
		event.Skip()

	def on_edit_data( self, event ):
		event.Skip()

	def on_calc_carga( self, event ):
		event.Skip()

	def on_calc_distancias_minimas( self, event ):
		event.Skip()

	def on_calc_centro_carga( self, event ):
		event.Skip()

	def on_buscar_tags( self, event ):
		event.Skip()

	def on_buscar_espacios( self, event ):
		event.Skip()

	def on_calcular_controles( self, event ):
		event.Skip()

	def on_context_menu_treectrl( self, event ):
		event.Skip()

	def on_click( self, event ):
		event.Skip()

	def on_click_tags( self, event ):
		event.Skip()

	def on_click_ramas( self, event ):
		event.Skip()

	def on_left_down( self, event ):
		event.Skip()

	def on_mouse_motion( self, event ):
		event.Skip()

	def on_paint( self, event ):
		event.Skip()

	def on_context_menu( self, event ):
		event.Skip()

	def on_save( self, event ):
		event.Skip()

	def on_open( self, event ):
		event.Skip()

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 337 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )

	def m_splitter31OnIdle( self, event ):
		self.m_splitter31.SetSashPosition( 165 )
		self.m_splitter31.Unbind( wx.EVT_IDLE )

	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 0 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )

	def m_splitter5OnIdle( self, event ):
		self.m_splitter5.SetSashPosition( 208 )
		self.m_splitter5.Unbind( wx.EVT_IDLE )

	def m_splitter6OnIdle( self, event ):
		self.m_splitter6.SetSashPosition( 0 )
		self.m_splitter6.Unbind( wx.EVT_IDLE )


###########################################################################
## Class Distancia
###########################################################################

class Distancia ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 256,62 ), style = wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Distancia en metros", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.on_enter )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_enter( self, event ):
		event.Skip()


###########################################################################
## Class GestorElementos
###########################################################################

class GestorElementos ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 200,308 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,230 ), wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		m_comboBox1Choices = [ u"Centro de carga", u"Placa de accesorios", u"Lampara de techo", u"Lampara de piso", u"Lampara de pared", wx.EmptyString ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer52.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"tipo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer52.Add( self.m_staticText22, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer52, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_x = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_x, 1, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_y = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_textCtrl_y, 1, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer51.Add( self.m_staticText21, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer51, 0, wx.EXPAND, 5 )

		bSizer5111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_z = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5111.Add( self.m_textCtrl_z, 1, wx.ALL, 5 )

		self.m_staticText2111 = wx.StaticText( self, wx.ID_ANY, u"z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )

		bSizer5111.Add( self.m_staticText2111, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5111, 1, wx.EXPAND, 5 )

		bSizer511 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_potencia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer511.Add( self.m_textCtrl_potencia, 1, wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"potencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer511.Add( self.m_staticText211, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer511, 0, wx.EXPAND, 5 )

		bSizer5112 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_tag = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5112.Add( self.m_textCtrl_tag, 1, wx.ALL, 5 )

		self.m_staticText2112 = wx.StaticText( self, wx.ID_ANY, u"tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2112.Wrap( -1 )

		bSizer5112.Add( self.m_staticText2112, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5112, 1, wx.EXPAND, 5 )

		bSizer5113 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_espacio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5113.Add( self.m_textCtrl_espacio, 1, wx.ALL, 5 )

		self.m_staticText2113 = wx.StaticText( self, wx.ID_ANY, u"espacio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2113.Wrap( -1 )

		bSizer5113.Add( self.m_staticText2113, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5113, 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.on_choice )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_ok )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_choice( self, event ):
		event.Skip()

	def on_ok( self, event ):
		event.Skip()



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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1466,862 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 957,862 ), wx.DefaultSize )

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

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_distancia = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_textCtrl_distancia, 1, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_panel6, wx.ID_ANY, u"Calc Distancias", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_button21, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer141, 0, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"Propuestas de diseño" ), wx.VERTICAL )

		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl10 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrl10, 1, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"lamp-lamp mismo tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer30.Add( self.m_staticText9, 0, wx.ALL, 5 )


		gSizer21.Add( bSizer30, 1, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl11 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_textCtrl11, 1, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"acc-lamp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer31.Add( self.m_staticText10, 0, wx.ALL, 5 )


		gSizer21.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl12 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_textCtrl12, 1, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"acc_cc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer32.Add( self.m_staticText11, 0, wx.ALL, 5 )


		gSizer21.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl13 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_textCtrl13, 1, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"lamp-lamp diff tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer33.Add( self.m_staticText12, 0, wx.ALL, 5 )


		gSizer21.Add( bSizer33, 1, wx.EXPAND, 5 )


		sbSizer3.Add( gSizer21, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button6 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Proponer red", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button6, 1, wx.ALL, 5 )

		self.m_button9 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Sugerir alimentadores", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button9, 1, wx.ALL, 5 )


		sbSizer3.Add( bSizer34, 0, wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"opciones de calculo" ), wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"No unir placas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		gSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )


		sbSizer1.Add( gSizer2, 0, 0, 5 )


		sbSizer3.Add( sbSizer1, 0, wx.EXPAND, 5 )


		bSizer13.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"analisis de controles" ), wx.HORIZONTAL )

		m_radioBox1Choices = [ u"Regreso de control mas cercano", u"Fase de control mas cercano" ]
		self.m_radioBox1 = wx.RadioBox( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Opciones para regreso", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 1 )
		sbSizer31.Add( self.m_radioBox1, 1, wx.ALL, 5 )

		self.m_button7 = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Verificar controles", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer31.Add( self.m_button7, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( sbSizer31, 0, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer13 )
		self.m_panel6.Layout()
		bSizer13.Fit( self.m_panel6 )
		self.m_splitter31.SplitHorizontally( self.m_panel5, self.m_panel6, 151 )
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

		self.m_panel9 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		self.m_splitter6.SplitVertically( self.m_panel11, self.m_panel12, 50 )
		bSizer21.Add( self.m_splitter6, 1, wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer21 )
		self.m_panel9.Layout()
		bSizer21.Fit( self.m_panel9 )
		bSizer20.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer20 )
		self.m_panel8.Layout()
		bSizer20.Fit( self.m_panel8 )
		self.m_splitter4.SplitVertically( self.m_panel7, self.m_panel8, 50 )
		bSizer19.Add( self.m_splitter4, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer19 )
		self.m_panel4.Layout()
		bSizer19.Fit( self.m_panel4 )
		self.m_splitter3.SplitHorizontally( self.m_panel3, self.m_panel4, 466 )
		bSizer2.Add( self.m_splitter3, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_panel16 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter8 = wx.SplitterWindow( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter8.Bind( wx.EVT_IDLE, self.m_splitter8OnIdle )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer351 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1500,1500 ), wx.TAB_TRAVERSAL )
		bSizer351.Add( self.m_panel2, 0, wx.ALIGN_CENTER, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer351 )
		self.m_scrolledWindow1.Layout()
		bSizer351.Fit( self.m_scrolledWindow1 )
		self.m_panel18 = wx.Panel( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter7 = wx.SplitterWindow( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter7.Bind( wx.EVT_IDLE, self.m_splitter7OnIdle )

		self.m_panel13 = wx.Panel( self.m_splitter7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 0, 3 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 80 )
		self.m_grid1.SetColSize( 1, 63 )
		self.m_grid1.SetColSize( 2, 130 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelValue( 0, u"Espacio" )
		self.m_grid1.SetColLabelValue( 1, u"Circuito" )
		self.m_grid1.SetColLabelValue( 2, u"Centro de carga sugerido" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer25.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel13.SetSizer( bSizer25 )
		self.m_panel13.Layout()
		bSizer25.Fit( self.m_panel13 )
		self.m_panel14 = wx.Panel( self.m_splitter7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter81 = wx.SplitterWindow( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter81.Bind( wx.EVT_IDLE, self.m_splitter81OnIdle )

		self.m_panel161 = wx.Panel( self.m_splitter81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel161, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 0, 6 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 64 )
		self.m_grid2.SetColSize( 1, 57 )
		self.m_grid2.SetColSize( 2, 120 )
		self.m_grid2.SetColSize( 3, 68 )
		self.m_grid2.SetColSize( 4, 80 )
		self.m_grid2.SetColSize( 5, 80 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelValue( 0, u"Circuito" )
		self.m_grid2.SetColLabelValue( 1, u"Carga" )
		self.m_grid2.SetColLabelValue( 2, u"Centro de carga" )
		self.m_grid2.SetColLabelValue( 3, u"Corriente" )
		self.m_grid2.SetColLabelValue( 4, u"Cable I" )
		self.m_grid2.SetColLabelValue( 5, u"Cable V" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer35.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel161.SetSizer( bSizer35 )
		self.m_panel161.Layout()
		bSizer35.Fit( self.m_panel161 )
		self.m_panel17 = wx.Panel( self.m_splitter81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_carga = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl_carga, 1, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel17, wx.ID_ANY, u"Calc Carga", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer36.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self.m_panel17, wx.ID_ANY, u"Calcular centro carga", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self.m_panel17, wx.ID_ANY, u"Forzar cc por circuito", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button81 = wx.Button( self.m_panel17, wx.ID_ANY, u"Asignar cc mas cercano", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button81, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self.m_panel17, wx.ID_ANY, u"Sugerir cc por espacio", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self.m_panel17, wx.ID_ANY, u"Calcular flujo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel17, wx.ID_ANY, u"Calcular cableado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button13.SetBackgroundColour( wx.Colour( 7, 149, 0 ) )

		bSizer24.Add( self.m_button13, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel17, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.m_button131 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Calcular cuadro de cargas por cc", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button131, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox2Choices = [ u"Monofasico", u"Bifasico", u"Trifasico" ]
		self.m_radioBox2 = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox2.SetSelection( 1 )
		sbSizer4.Add( self.m_radioBox2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer24.Add( sbSizer4, 1, wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self.m_panel17, wx.ID_ANY, u"Dimensionar por caida de tension", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button14, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer36.Add( bSizer24, 0, wx.EXPAND, 5 )


		self.m_panel17.SetSizer( bSizer36 )
		self.m_panel17.Layout()
		bSizer36.Fit( self.m_panel17 )
		self.m_splitter81.SplitHorizontally( self.m_panel161, self.m_panel17, 190 )
		bSizer26.Add( self.m_splitter81, 1, wx.EXPAND, 5 )


		self.m_panel14.SetSizer( bSizer26 )
		self.m_panel14.Layout()
		bSizer26.Fit( self.m_panel14 )
		self.m_splitter7.SplitHorizontally( self.m_panel13, self.m_panel14, 124 )
		bSizer28.Add( self.m_splitter7, 1, wx.EXPAND, 5 )


		self.m_panel18.SetSizer( bSizer28 )
		self.m_panel18.Layout()
		bSizer28.Fit( self.m_panel18 )
		self.m_splitter8.SplitVertically( self.m_scrolledWindow1, self.m_panel18, 552 )
		bSizer27.Add( self.m_splitter8, 1, wx.EXPAND, 5 )


		self.m_panel16.SetSizer( bSizer27 )
		self.m_panel16.Layout()
		bSizer27.Fit( self.m_panel16 )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel16, 518 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool5 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/importar.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/actualizar.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/ojo.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None )

		self.m_tool51 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/x.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool61 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"img/print.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar2.Realize()

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Cotizar enmanguerado", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"Cotizaciones" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.on_change_size )
		self.m_splitter1.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.on_sash_changed )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_change )
		self.m_dataViewListCtrl.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.on_edit_data, id = wx.ID_ANY )
		self.m_button21.Bind( wx.EVT_BUTTON, self.on_calc_distancias )
		self.m_button6.Bind( wx.EVT_BUTTON, self.on_ver_red )
		self.m_button9.Bind( wx.EVT_BUTTON, self.on_calcular_alimentadores )
		self.m_button7.Bind( wx.EVT_BUTTON, self.on_verificar_controles )
		self.m_treeCtrl.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.on_context_menu_treectrl )
		self.m_treeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click )
		self.m_treeCtrl_tags.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click_tags )
		self.m_treeCtrl_ramas.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.on_context_menu_treectrl_ramas )
		self.m_treeCtrl_ramas.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_click_ramas )
		self.m_scrolledWindow1.Bind( wx.EVT_MOUSEWHEEL, self.on_mouse_wheel )
		self.m_panel2.Bind( wx.EVT_LEFT_DOWN, self.on_left_down )
		self.m_panel2.Bind( wx.EVT_MOTION, self.on_mouse_motion )
		self.m_panel2.Bind( wx.EVT_PAINT, self.on_paint )
		self.m_panel2.Bind( wx.EVT_RIGHT_DOWN, self.on_context_menu )
		self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.recalcular )
		self.m_grid2.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.on_cc_force_change )
		self.m_grid2.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_click_circuito )
		self.m_button2.Bind( wx.EVT_BUTTON, self.on_calc_carga )
		self.m_button3.Bind( wx.EVT_BUTTON, self.on_calc_centro_carga )
		self.m_button11.Bind( wx.EVT_BUTTON, self.on_asignar_cc )
		self.m_button81.Bind( wx.EVT_BUTTON, self.on_propose_alimentacion )
		self.m_button10.Bind( wx.EVT_BUTTON, self.on_calcular_cc_preferido )
		self.m_button12.Bind( wx.EVT_BUTTON, self.on_calcular_flujos )
		self.m_button13.Bind( wx.EVT_BUTTON, self.on_calcular_cableado )
		self.m_button131.Bind( wx.EVT_BUTTON, self.on_calcular_cuadro_carga_x_cc )
		self.m_button14.Bind( wx.EVT_BUTTON, self.on_caida_tension )
		self.Bind( wx.EVT_TOOL, self.on_save, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_open, id = self.m_tool6.GetId() )
		self.Bind( wx.EVT_TOOL, self.recalcular, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_ver, id = self.m_tool4.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_clean_trayectorias, id = self.m_tool51.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_save_img, id = self.m_tool61.GetId() )
		self.Bind( wx.EVT_MENU, self.on_cotizar_enmanguerado, id = self.m_menuItem1.GetId() )

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

	def on_calc_distancias( self, event ):
		event.Skip()

	def on_ver_red( self, event ):
		event.Skip()

	def on_calcular_alimentadores( self, event ):
		event.Skip()

	def on_verificar_controles( self, event ):
		event.Skip()

	def on_context_menu_treectrl( self, event ):
		event.Skip()

	def on_click( self, event ):
		event.Skip()

	def on_click_tags( self, event ):
		event.Skip()

	def on_context_menu_treectrl_ramas( self, event ):
		event.Skip()

	def on_click_ramas( self, event ):
		event.Skip()

	def on_mouse_wheel( self, event ):
		event.Skip()

	def on_left_down( self, event ):
		event.Skip()

	def on_mouse_motion( self, event ):
		event.Skip()

	def on_paint( self, event ):
		event.Skip()

	def on_context_menu( self, event ):
		event.Skip()

	def recalcular( self, event ):
		event.Skip()

	def on_cc_force_change( self, event ):
		event.Skip()

	def on_click_circuito( self, event ):
		event.Skip()

	def on_calc_carga( self, event ):
		event.Skip()

	def on_calc_centro_carga( self, event ):
		event.Skip()

	def on_asignar_cc( self, event ):
		event.Skip()

	def on_propose_alimentacion( self, event ):
		event.Skip()

	def on_calcular_cc_preferido( self, event ):
		event.Skip()

	def on_calcular_flujos( self, event ):
		event.Skip()

	def on_calcular_cableado( self, event ):
		event.Skip()

	def on_calcular_cuadro_carga_x_cc( self, event ):
		event.Skip()

	def on_caida_tension( self, event ):
		event.Skip()

	def on_save( self, event ):
		event.Skip()

	def on_open( self, event ):
		event.Skip()


	def on_ver( self, event ):
		event.Skip()

	def on_clean_trayectorias( self, event ):
		event.Skip()

	def on_save_img( self, event ):
		event.Skip()

	def on_cotizar_enmanguerado( self, event ):
		event.Skip()

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 518 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 466 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )

	def m_splitter31OnIdle( self, event ):
		self.m_splitter31.SetSashPosition( 151 )
		self.m_splitter31.Unbind( wx.EVT_IDLE )

	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 50 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )

	def m_splitter6OnIdle( self, event ):
		self.m_splitter6.SetSashPosition( 50 )
		self.m_splitter6.Unbind( wx.EVT_IDLE )

	def m_splitter8OnIdle( self, event ):
		self.m_splitter8.SetSashPosition( 552 )
		self.m_splitter8.Unbind( wx.EVT_IDLE )

	def m_splitter7OnIdle( self, event ):
		self.m_splitter7.SetSashPosition( 124 )
		self.m_splitter7.Unbind( wx.EVT_IDLE )

	def m_splitter81OnIdle( self, event ):
		self.m_splitter81.SetSashPosition( 190 )
		self.m_splitter81.Unbind( wx.EVT_IDLE )


###########################################################################
## Class CuadroCarga
###########################################################################

class CuadroCarga ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 557,368 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter9 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter9.Bind( wx.EVT_IDLE, self.m_splitter9OnIdle )

		self.m_panel19 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self.m_panel19, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		bSizer38.Add( self.m_comboBox2, 0, wx.ALL, 5 )

		self.m_grid3 = wx.grid.Grid( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 1, 1 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer38.Add( self.m_grid3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel19.SetSizer( bSizer38 )
		self.m_panel19.Layout()
		bSizer38.Fit( self.m_panel19 )
		self.m_panel21 = wx.Panel( self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"Desbalanceo" ), wx.VERTICAL )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid5 = wx.grid.Grid( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid5.CreateGrid( 1, 1 )
		self.m_grid5.EnableEditing( False )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )

		# Columns
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer39.Add( self.m_grid5, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( bSizer39, 1, wx.EXPAND, 5 )


		self.m_panel21.SetSizer( sbSizer5 )
		self.m_panel21.Layout()
		sbSizer5.Fit( self.m_panel21 )
		self.m_splitter9.SplitHorizontally( self.m_panel19, self.m_panel21, 184 )
		bSizer37.Add( self.m_splitter9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer37 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.on_combo_box )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_combo_box( self, event ):
		event.Skip()

	def m_splitter9OnIdle( self, event ):
		self.m_splitter9.SetSashPosition( 184 )
		self.m_splitter9.Unbind( wx.EVT_IDLE )


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



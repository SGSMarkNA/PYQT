import PYQT

# ########################################################################
# class AnchorAttribute:
	# AnchorName = PYQT.Qt.AnchorName
	# AnchorHref = PYQT.Qt.AnchorHref
########################################################################
class AnchorPoint:
	AnchorBottom                      = PYQT.Qt.AnchorBottom
	AnchorRight                       = PYQT.Qt.AnchorRight
	AnchorLeft                        = PYQT.Qt.AnchorLeft
	AnchorHorizontalCenter            = PYQT.Qt.AnchorHorizontalCenter
	AnchorTop                         = PYQT.Qt.AnchorTop
	AnchorVerticalCenter              = PYQT.Qt.AnchorVerticalCenter
########################################################################
class ApplicationAttribute:
	AA_DontShowIconsInMenus           = PYQT.Qt.AA_DontShowIconsInMenus
	AA_DontUseNativeMenuBar           = PYQT.Qt.AA_DontUseNativeMenuBar
	AA_NativeWindows                  = PYQT.Qt.AA_NativeWindows
	AA_ImmediateWidgetCreation        = PYQT.Qt.AA_ImmediateWidgetCreation
	AA_MSWindowsUseDirect3DByDefault  = PYQT.Qt.AA_MSWindowsUseDirect3DByDefault
	# AA_S60DontConstructApplicationPanes = PYQT.Qt.AA_DontConstructApplicationPanes
	AA_DontCreateNativeWidgetSiblings = PYQT.Qt.AA_DontCreateNativeWidgetSiblings
	AA_MacDontSwapCtrlAndMeta         = PYQT.Qt.AA_MacDontSwapCtrlAndMeta
	AA_MacPluginApplication           = PYQT.Qt.AA_MacPluginApplication
########################################################################
class ArrowType:
	RightArrow                        = PYQT.Qt.RightArrow
	NoArrow                           = PYQT.Qt.NoArrow
	UpArrow                           = PYQT.Qt.UpArrow
	DownArrow                         = PYQT.Qt.DownArrow
	LeftArrow                         = PYQT.Qt.LeftArrow
########################################################################
class AspectRatioMode:
	IgnoreAspectRatio                 = PYQT.Qt.IgnoreAspectRatio
	KeepAspectRatio                   = PYQT.Qt.KeepAspectRatio
	KeepAspectRatioByExpanding        = PYQT.Qt.KeepAspectRatioByExpanding
########################################################################
class Axis:
	ZAxis                             = PYQT.Qt.ZAxis
	XAxis                             = PYQT.Qt.XAxis
	YAxis                             = PYQT.Qt.YAxis
########################################################################
class BGMode:
	TransparentMode                   = PYQT.Qt.TransparentMode
	OpaqueMode                        = PYQT.Qt.OpaqueMode
########################################################################
class CaseSensitivity:
	CaseSensitive                     = PYQT.Qt.CaseSensitive
	CaseInsensitive                   = PYQT.Qt.CaseInsensitive
########################################################################
class ClipOperation:
	# UniteClip     = PYQT.Qt.UniteClip
	ReplaceClip                       = PYQT.Qt.ReplaceClip
	IntersectClip                     = PYQT.Qt.IntersectClip
	NoClip                            = PYQT.Qt.NoClip
########################################################################
class ConnectionType:
	UniqueConnection                  = PYQT.Qt.UniqueConnection
	AutoConnection                    = PYQT.Qt.AutoConnection
	BlockingQueuedConnection          = PYQT.Qt.BlockingQueuedConnection
	QueuedConnection                  = PYQT.Qt.QueuedConnection
	# AutoCompatConnection     = PYQT.Qt.AutoCompatConnection
	DirectConnection                  = PYQT.Qt.DirectConnection
########################################################################
class ContextMenuPolicy:
	DefaultContextMenu                = PYQT.Qt.DefaultContextMenu
	PreventContextMenu                = PYQT.Qt.PreventContextMenu
	ActionsContextMenu                = PYQT.Qt.ActionsContextMenu
	NoContextMenu                     = PYQT.Qt.NoContextMenu
	CustomContextMenu                 = PYQT.Qt.CustomContextMenu
########################################################################
class CoordinateSystem:
	LogicalCoordinates                = PYQT.Qt.LogicalCoordinates
	DeviceCoordinates                 = PYQT.Qt.DeviceCoordinates
########################################################################
class Corner:
	TopRightCorner                    = PYQT.Qt.TopRightCorner
	BottomRightCorner                 = PYQT.Qt.BottomRightCorner
	TopLeftCorner                     = PYQT.Qt.TopLeftCorner
	BottomLeftCorner                  = PYQT.Qt.BottomLeftCorner
########################################################################
class CursorShape:
	DragCopyCursor                    = PYQT.Qt.DragCopyCursor
	CrossCursor                       = PYQT.Qt.CrossCursor
	SizeFDiagCursor                   = PYQT.Qt.SizeFDiagCursor
	SizeAllCursor                     = PYQT.Qt.SizeAllCursor
	SizeHorCursor                     = PYQT.Qt.SizeHorCursor
	UpArrowCursor                     = PYQT.Qt.UpArrowCursor
	CustomCursor                      = PYQT.Qt.CustomCursor
	LastCursor                        = PYQT.Qt.LastCursor
	BusyCursor                        = PYQT.Qt.BusyCursor
	OpenHandCursor                    = PYQT.Qt.OpenHandCursor
	SizeVerCursor                     = PYQT.Qt.SizeVerCursor
	WhatsThisCursor                   = PYQT.Qt.WhatsThisCursor
	BitmapCursor                      = PYQT.Qt.BitmapCursor
	DragMoveCursor                    = PYQT.Qt.DragMoveCursor
	DragLinkCursor                    = PYQT.Qt.DragLinkCursor
	IBeamCursor                       = PYQT.Qt.IBeamCursor
	ArrowCursor                       = PYQT.Qt.ArrowCursor
	SplitVCursor                      = PYQT.Qt.SplitVCursor
	WaitCursor                        = PYQT.Qt.WaitCursor
	BlankCursor                       = PYQT.Qt.BlankCursor
	PointingHandCursor                = PYQT.Qt.PointingHandCursor
	ForbiddenCursor                   = PYQT.Qt.ForbiddenCursor
	SizeBDiagCursor                   = PYQT.Qt.SizeBDiagCursor
	SplitHCursor                      = PYQT.Qt.SplitHCursor
	ClosedHandCursor                  = PYQT.Qt.ClosedHandCursor
########################################################################
class DateFormat:
	DefaultLocaleLongDate             = PYQT.Qt.DefaultLocaleLongDate
	TextDate                          = PYQT.Qt.TextDate
	LocaleDate                        = PYQT.Qt.LocaleDate
	ISODate                           = PYQT.Qt.ISODate
	DefaultLocaleShortDate            = PYQT.Qt.DefaultLocaleShortDate
	SystemLocaleShortDate             = PYQT.Qt.SystemLocaleShortDate
	LocalDate                         = PYQT.Qt.LocalDate
	SystemLocaleDate                  = PYQT.Qt.SystemLocaleDate
	SystemLocaleLongDate              = PYQT.Qt.SystemLocaleLongDate
########################################################################
class DockWidgetArea:
	AllDockWidgetAreas                = PYQT.Qt.AllDockWidgetAreas
	LeftDockWidgetArea                = PYQT.Qt.LeftDockWidgetArea
	DockWidgetArea_Mask               = PYQT.Qt.DockWidgetArea_Mask
	NoDockWidgetArea                  = PYQT.Qt.NoDockWidgetArea
	TopDockWidgetArea                 = PYQT.Qt.TopDockWidgetArea
	RightDockWidgetArea               = PYQT.Qt.RightDockWidgetArea
	BottomDockWidgetArea              = PYQT.Qt.BottomDockWidgetArea
########################################################################
class DropAction:
	LinkAction                        = PYQT.Qt.LinkAction
	CopyAction                        = PYQT.Qt.CopyAction
	IgnoreAction                      = PYQT.Qt.IgnoreAction
	TargetMoveAction                  = PYQT.Qt.TargetMoveAction
	MoveAction                        = PYQT.Qt.MoveAction
	ActionMask                        = PYQT.Qt.ActionMask
########################################################################
class EventPriority:
	NormalEventPriority               = PYQT.Qt.NormalEventPriority
	HighEventPriority                 = PYQT.Qt.HighEventPriority
	LowEventPriority                  = PYQT.Qt.LowEventPriority
########################################################################
class FillRule:
	WindingFill                       = PYQT.Qt.WindingFill
	OddEvenFill                       = PYQT.Qt.OddEvenFill
########################################################################
class FocusPolicy:
	StrongFocus                       = PYQT.Qt.StrongFocus
	WheelFocus                        = PYQT.Qt.WheelFocus
	ClickFocus                        = PYQT.Qt.ClickFocus
	TabFocus                          = PYQT.Qt.TabFocus
	NoFocus                           = PYQT.Qt.NoFocus
########################################################################
class FocusReason:
	NoFocusReason                     = PYQT.Qt.NoFocusReason
	BacktabFocusReason                = PYQT.Qt.BacktabFocusReason
	ShortcutFocusReason               = PYQT.Qt.ShortcutFocusReason
	PopupFocusReason                  = PYQT.Qt.PopupFocusReason
	MouseFocusReason                  = PYQT.Qt.MouseFocusReason
	ActiveWindowFocusReason           = PYQT.Qt.ActiveWindowFocusReason
	MenuBarFocusReason                = PYQT.Qt.MenuBarFocusReason
	TabFocusReason                    = PYQT.Qt.TabFocusReason
	OtherFocusReason                  = PYQT.Qt.OtherFocusReason
########################################################################
class GestureFlag:
	DontStartGestureOnChildren        = PYQT.Qt.DontStartGestureOnChildren
	ReceivePartialGestures            = PYQT.Qt.ReceivePartialGestures
	IgnoredGesturesPropagateToParent  = PYQT.Qt.IgnoredGesturesPropagateToParent
########################################################################
class GestureState:
	GestureUpdated                    = PYQT.Qt.GestureUpdated
	GestureFinished                   = PYQT.Qt.GestureFinished
	GestureCanceled                   = PYQT.Qt.GestureCanceled
	GestureStarted                    = PYQT.Qt.GestureStarted
########################################################################
class GestureType:
	SwipeGesture                      = PYQT.Qt.SwipeGesture
	CustomGesture                     = PYQT.Qt.CustomGesture
	PinchGesture                      = PYQT.Qt.PinchGesture
	TapAndHoldGesture                 = PYQT.Qt.TapAndHoldGesture
	TapGesture                        = PYQT.Qt.TapGesture
	PanGesture                        = PYQT.Qt.PanGesture
########################################################################
class GlobalColor:
	lightGray                         = PYQT.Qt.lightGray
	gray                              = PYQT.Qt.gray
	darkGreen                         = PYQT.Qt.darkGreen
	darkMagenta                       = PYQT.Qt.darkMagenta
	darkCyan                          = PYQT.Qt.darkCyan
	darkBlue                          = PYQT.Qt.darkBlue
	darkGray                          = PYQT.Qt.darkGray
	blue                              = PYQT.Qt.blue
	yellow                            = PYQT.Qt.yellow
	darkYellow                        = PYQT.Qt.darkYellow
	color1                            = PYQT.Qt.color1
	color0                            = PYQT.Qt.color0
	transparent                       = PYQT.Qt.transparent
	black                             = PYQT.Qt.black
	darkRed                           = PYQT.Qt.darkRed
	cyan                              = PYQT.Qt.cyan
	green                             = PYQT.Qt.green
	white                             = PYQT.Qt.white
	magenta                           = PYQT.Qt.magenta
	red                               = PYQT.Qt.red
########################################################################
class HitTestAccuracy:
	FuzzyHit                          = PYQT.Qt.FuzzyHit
	ExactHit                          = PYQT.Qt.ExactHit
########################################################################
class ImageConversionFlag:
	AvoidDither                       = PYQT.Qt.AvoidDither
	AutoColor                         = PYQT.Qt.AutoColor
	OrderedDither                     = PYQT.Qt.OrderedDither
	PreferDither                      = PYQT.Qt.PreferDither
	OrderedAlphaDither                = PYQT.Qt.OrderedAlphaDither
	ThresholdAlphaDither              = PYQT.Qt.ThresholdAlphaDither
	DiffuseAlphaDither                = PYQT.Qt.DiffuseAlphaDither
	DiffuseDither                     = PYQT.Qt.DiffuseDither
	AutoDither                        = PYQT.Qt.AutoDither
	ColorOnly                         = PYQT.Qt.ColorOnly
	MonoOnly                          = PYQT.Qt.MonoOnly
	ThresholdDither                   = PYQT.Qt.ThresholdDither
########################################################################
class InputMethodHint:
	ImhPreferNumbers                  = PYQT.Qt.ImhPreferNumbers
	ImhDialableCharactersOnly         = PYQT.Qt.ImhDialableCharactersOnly
	ImhNoAutoUppercase                = PYQT.Qt.ImhNoAutoUppercase
	ImhLowercaseOnly                  = PYQT.Qt.ImhLowercaseOnly
	ImhEmailCharactersOnly            = PYQT.Qt.ImhEmailCharactersOnly
	ImhNoPredictiveText               = PYQT.Qt.ImhNoPredictiveText
	ImhUrlCharactersOnly              = PYQT.Qt.ImhUrlCharactersOnly
	ImhUppercaseOnly                  = PYQT.Qt.ImhUppercaseOnly
	ImhPreferUppercase                = PYQT.Qt.ImhPreferUppercase
	ImhDigitsOnly                     = PYQT.Qt.ImhDigitsOnly
	ImhFormattedNumbersOnly           = PYQT.Qt.ImhFormattedNumbersOnly
	ImhPreferLowercase                = PYQT.Qt.ImhPreferLowercase
	ImhHiddenText                     = PYQT.Qt.ImhHiddenText
	ImhNone                           = PYQT.Qt.ImhNone
	ImhExclusiveInputMask             = PYQT.Qt.ImhExclusiveInputMask
########################################################################
class InputMethodQuery:
	ImCursorPosition                  = PYQT.Qt.ImCursorPosition
	ImFont                            = PYQT.Qt.ImFont
	ImAnchorPosition                  = PYQT.Qt.ImAnchorPosition
	ImMicroFocus                      = PYQT.Qt.ImMicroFocus
	ImMaximumTextLength               = PYQT.Qt.ImMaximumTextLength
	ImSurroundingText                 = PYQT.Qt.ImSurroundingText
	ImCurrentSelection                = PYQT.Qt.ImCurrentSelection
########################################################################
class ItemSelectionMode:
	ContainsItemBoundingRect          = PYQT.Qt.ContainsItemBoundingRect
	IntersectsItemBoundingRect        = PYQT.Qt.IntersectsItemBoundingRect
	ContainsItemShape                 = PYQT.Qt.ContainsItemShape
	IntersectsItemShape               = PYQT.Qt.IntersectsItemShape
########################################################################
class Key:
	Excel                             = PYQT.Qt.Key_Excel
	hyphen                            = PYQT.Qt.Key_hyphen
	Space                             = PYQT.Qt.Key_Space
	Pause                             = PYQT.Qt.Key_Pause
	F27                               = PYQT.Qt.Key_F27
	F26                               = PYQT.Qt.Key_F26
	F25                               = PYQT.Qt.Key_F25
	F24                               = PYQT.Qt.Key_F24
	F23                               = PYQT.Qt.Key_F23
	F22                               = PYQT.Qt.Key_F22
	F21                               = PYQT.Qt.Key_F21
	F20                               = PYQT.Qt.Key_F20
	DOS                               = PYQT.Qt.Key_DOS
	F29                               = PYQT.Qt.Key_F29
	F28                               = PYQT.Qt.Key_F28
	OpenUrl                           = PYQT.Qt.Key_OpenUrl
	Launch8                           = PYQT.Qt.Key_Launch8
	Launch9                           = PYQT.Qt.Key_Launch9
	Dead_Belowdot                     = PYQT.Qt.Key_Dead_Belowdot
	onequarter                        = PYQT.Qt.Key_onequarter
	HomePage                          = PYQT.Qt.Key_HomePage
	Launch1                           = PYQT.Qt.Key_Launch1
	Launch2                           = PYQT.Qt.Key_Launch2
	Launch3                           = PYQT.Qt.Key_Launch3
	Launch4                           = PYQT.Qt.Key_Launch4
	Launch5                           = PYQT.Qt.Key_Launch5
	Launch6                           = PYQT.Qt.Key_Launch6
	Launch7                           = PYQT.Qt.Key_Launch7
	LaunchH                           = PYQT.Qt.Key_LaunchH
	Ediaeresis                        = PYQT.Qt.Key_Ediaeresis
	Shift                             = PYQT.Qt.Key_Shift
	LaunchA                           = PYQT.Qt.Key_LaunchA
	LaunchB                           = PYQT.Qt.Key_LaunchB
	LaunchC                           = PYQT.Qt.Key_LaunchC
	LaunchD                           = PYQT.Qt.Key_LaunchD
	LaunchE                           = PYQT.Qt.Key_LaunchE
	LaunchF                           = PYQT.Qt.Key_LaunchF
	LaunchG                           = PYQT.Qt.Key_LaunchG
	Left                              = PYQT.Qt.Key_Left
	Dead_Caron                        = PYQT.Qt.Key_Dead_Caron
	Hangul_Special                    = PYQT.Qt.Key_Hangul_Special
	Hangul_Jamo                       = PYQT.Qt.Key_Hangul_Jamo
	Period                            = PYQT.Qt.Key_Period
	Dead_Voiced_Sound                 = PYQT.Qt.Key_Dead_Voiced_Sound
	Ooblique                          = PYQT.Qt.Key_Ooblique
	OfficeHome                        = PYQT.Qt.Key_OfficeHome
	Colon                             = PYQT.Qt.Key_Colon
	Forward                           = PYQT.Qt.Key_Forward
	UWB                               = PYQT.Qt.Key_UWB
	Katakana                          = PYQT.Qt.Key_Katakana
	Eisu_toggle                       = PYQT.Qt.Key_Eisu_toggle
	Zoom                              = PYQT.Qt.Key_Zoom
	Zenkaku                           = PYQT.Qt.Key_Zenkaku
	Save                              = PYQT.Qt.Key_Save
	Greater                           = PYQT.Qt.Key_Greater
	WebCam                            = PYQT.Qt.Key_WebCam
	VolumeMute                        = PYQT.Qt.Key_VolumeMute
	ParenRight                        = PYQT.Qt.Key_ParenRight
	MenuKB                            = PYQT.Qt.Key_MenuKB
	Video                             = PYQT.Qt.Key_Video
	Oacute                            = PYQT.Qt.Key_Oacute
	NumLock                           = PYQT.Qt.Key_NumLock
	Multi_key                         = PYQT.Qt.Key_Multi_key
	Ugrave                            = PYQT.Qt.Key_Ugrave
	Ccedilla                          = PYQT.Qt.Key_Ccedilla
	Dead_Horn                         = PYQT.Qt.Key_Dead_Horn
	Hangul_Hanja                      = PYQT.Qt.Key_Hangul_Hanja
	Call                              = PYQT.Qt.Key_Call
	AudioForward                      = PYQT.Qt.Key_AudioForward
	macron                            = PYQT.Qt.Key_macron
	section                           = PYQT.Qt.Key_section
	Away                              = PYQT.Qt.Key_Away
	MenuPB                            = PYQT.Qt.Key_MenuPB
	Hangul_Jeonja                     = PYQT.Qt.Key_Hangul_Jeonja
	Equal                             = PYQT.Qt.Key_Equal
	Standby                           = PYQT.Qt.Key_Standby
	TrebleDown                        = PYQT.Qt.Key_TrebleDown
	Launch0                           = PYQT.Qt.Key_Launch0
	Hankaku                           = PYQT.Qt.Key_Hankaku
	Enter                             = PYQT.Qt.Key_Enter
	Dead_Semivoiced_Sound             = PYQT.Qt.Key_Dead_Semivoiced_Sound
	Dead_Tilde                        = PYQT.Qt.Key_Dead_Tilde
	ScreenSaver                       = PYQT.Qt.Key_ScreenSaver
	Less                              = PYQT.Qt.Key_Less
	Game                              = PYQT.Qt.Key_Game
	Alt                               = PYQT.Qt.Key_Alt
	yen                               = PYQT.Qt.Key_yen
	NumberSign                        = PYQT.Qt.Key_NumberSign
	AudioRewind                       = PYQT.Qt.Key_AudioRewind
	Hangul_Banja                      = PYQT.Qt.Key_Hangul_Banja
	Printer                           = PYQT.Qt.Key_Printer
	twosuperior                       = PYQT.Qt.Key_twosuperior
	Favorites                         = PYQT.Qt.Key_Favorites
	Exclam                            = PYQT.Qt.Key_Exclam
	Xfer                              = PYQT.Qt.Key_Xfer
	AltGr                             = PYQT.Qt.Key_AltGr
	Kana_Lock                         = PYQT.Qt.Key_Kana_Lock
	Insert                            = PYQT.Qt.Key_Insert
	guillemotright                    = PYQT.Qt.Key_guillemotright
	Subtitle                          = PYQT.Qt.Key_Subtitle
	KeyboardBrightnessUp              = PYQT.Qt.Key_KeyboardBrightnessUp
	Market                            = PYQT.Qt.Key_Market
	MediaPause                        = PYQT.Qt.Key_MediaPause
	Suspend                           = PYQT.Qt.Key_Suspend
	VolumeDown                        = PYQT.Qt.Key_VolumeDown
	Send                              = PYQT.Qt.Key_Send
	ScrollLock                        = PYQT.Qt.Key_ScrollLock
	Travel                            = PYQT.Qt.Key_Travel
	BassDown                          = PYQT.Qt.Key_BassDown
	ApplicationLeft                   = PYQT.Qt.Key_ApplicationLeft
	BassBoost                         = PYQT.Qt.Key_BassBoost
	Hiragana                          = PYQT.Qt.Key_Hiragana
	TaskPane                          = PYQT.Qt.Key_TaskPane
	MediaTogglePlayPause              = PYQT.Qt.Key_MediaTogglePlayPause
	LastNumberRedial                  = PYQT.Qt.Key_LastNumberRedial
	Muhenkan                          = PYQT.Qt.Key_Muhenkan
	Option                            = PYQT.Qt.Key_Option
	masculine                         = PYQT.Qt.Key_masculine
	H                                 = PYQT.Qt.Key_H
	Phone                             = PYQT.Qt.Key_Phone
	AE                                = PYQT.Qt.Key_AE
	Refresh                           = PYQT.Qt.Key_Refresh
	MailForward                       = PYQT.Qt.Key_MailForward
	Super_R                           = PYQT.Qt.Key_Super_R
	F34                               = PYQT.Qt.Key_F34
	F35                               = PYQT.Qt.Key_F35
	F30                               = PYQT.Qt.Key_F30
	F31                               = PYQT.Qt.Key_F31
	F32                               = PYQT.Qt.Key_F32
	F33                               = PYQT.Qt.Key_F33
	Super_L                           = PYQT.Qt.Key_Super_L
	Dollar                            = PYQT.Qt.Key_Dollar
	ApplicationRight                  = PYQT.Qt.Key_ApplicationRight
	Backslash                         = PYQT.Qt.Key_Backslash
	Community                         = PYQT.Qt.Key_Community
	At                                = PYQT.Qt.Key_At
	Comma                             = PYQT.Qt.Key_Comma
	notsign                           = PYQT.Qt.Key_notsign
	LightBulb                         = PYQT.Qt.Key_LightBulb
	questiondown                      = PYQT.Qt.Key_questiondown
	QuoteLeft                         = PYQT.Qt.Key_QuoteLeft
	Hangul_PreHanja                   = PYQT.Qt.Key_Hangul_PreHanja
	Hangul_Romaja                     = PYQT.Qt.Key_Hangul_Romaja
	Calculator                        = PYQT.Qt.Key_Calculator
	ClearGrab                         = PYQT.Qt.Key_ClearGrab
	Eisu_Shift                        = PYQT.Qt.Key_Eisu_Shift
	cent                              = PYQT.Qt.Key_cent
	Messenger                         = PYQT.Qt.Key_Messenger
	Paste                             = PYQT.Qt.Key_Paste
	BraceRight                        = PYQT.Qt.Key_BraceRight
	Stop                              = PYQT.Qt.Key_Stop
	Sleep                             = PYQT.Qt.Key_Sleep
	KeyboardLightOnOff                = PYQT.Qt.Key_KeyboardLightOnOff
	VolumeUp                          = PYQT.Qt.Key_VolumeUp
	Ograve                            = PYQT.Qt.Key_Ograve
	Hangul_Start                      = PYQT.Qt.Key_Hangul_Start
	Codeinput                         = PYQT.Qt.Key_Codeinput
	Yes                               = PYQT.Qt.Key_Yes
	LaunchMedia                       = PYQT.Qt.Key_LaunchMedia
	exclamdown                        = PYQT.Qt.Key_exclamdown
	plusminus                         = PYQT.Qt.Key_plusminus
	Question                          = PYQT.Qt.Key_Question
	Context4                          = PYQT.Qt.Key_Context4
	Context3                          = PYQT.Qt.Key_Context3
	Context2                          = PYQT.Qt.Key_Context2
	Context1                          = PYQT.Qt.Key_Context1
	AsciiTilde                        = PYQT.Qt.Key_AsciiTilde
	BrightnessAdjust                  = PYQT.Qt.Key_BrightnessAdjust
	SingleCandidate                   = PYQT.Qt.Key_SingleCandidate
	Dead_Abovering                    = PYQT.Qt.Key_Dead_Abovering
	Finance                           = PYQT.Qt.Key_Finance
	Underscore                        = PYQT.Qt.Key_Underscore
	KeyboardBrightnessDown            = PYQT.Qt.Key_KeyboardBrightnessDown
	Dead_Breve                        = PYQT.Qt.Key_Dead_Breve
	Kanji                             = PYQT.Qt.Key_Kanji
	sterling                          = PYQT.Qt.Key_sterling
	Eject                             = PYQT.Qt.Key_Eject
	Copy                              = PYQT.Qt.Key_Copy
	Display                           = PYQT.Qt.Key_Display
	WWW                               = PYQT.Qt.Key_WWW
	HotLinks                          = PYQT.Qt.Key_HotLinks
	Agrave                            = PYQT.Qt.Key_Agrave
	Cut                               = PYQT.Qt.Key_Cut
	Idiaeresis                        = PYQT.Qt.Key_Idiaeresis
	acute                             = PYQT.Qt.Key_acute
	CameraFocus                       = PYQT.Qt.Key_CameraFocus
	Dead_Macron                       = PYQT.Qt.Key_Dead_Macron
	RotationPB                        = PYQT.Qt.Key_RotationPB
	Hibernate                         = PYQT.Qt.Key_Hibernate
	Return                            = PYQT.Qt.Key_Return
	Select                            = PYQT.Qt.Key_Select
	Dead_Diaeresis                    = PYQT.Qt.Key_Dead_Diaeresis
	PowerDown                         = PYQT.Qt.Key_PowerDown
	BracketLeft                       = PYQT.Qt.Key_BracketLeft
	Minus                             = PYQT.Qt.Key_Minus
	Apostrophe                        = PYQT.Qt.Key_Apostrophe
	Adiaeresis                        = PYQT.Qt.Key_Adiaeresis
	Shop                              = PYQT.Qt.Key_Shop
	WakeUp                            = PYQT.Qt.Key_WakeUp
	LaunchMail                        = PYQT.Qt.Key_LaunchMail
	End                               = PYQT.Qt.Key_End
	Otilde                            = PYQT.Qt.Key_Otilde
	TrebleUp                          = PYQT.Qt.Key_TrebleUp
	Pictures                          = PYQT.Qt.Key_Pictures
	BassUp                            = PYQT.Qt.Key_BassUp
	Ntilde                            = PYQT.Qt.Key_Ntilde
	Uacute                            = PYQT.Qt.Key_Uacute
	Zenkaku_Hankaku                   = PYQT.Qt.Key_Zenkaku_Hankaku
	Play                              = PYQT.Qt.Key_Play
	MySites                           = PYQT.Qt.Key_MySites
	Icircumflex                       = PYQT.Qt.Key_Icircumflex
	VoiceDial                         = PYQT.Qt.Key_VoiceDial
	Acircumflex                       = PYQT.Qt.Key_Acircumflex
	Dead_Grave                        = PYQT.Qt.Key_Dead_Grave
	Bar                               = PYQT.Qt.Key_Bar
	Backtab                           = PYQT.Qt.Key_Backtab
	History                           = PYQT.Qt.Key_History
	multiply                          = PYQT.Qt.Key_multiply
	Dead_Acute                        = PYQT.Qt.Key_Dead_Acute
	AudioRepeat                       = PYQT.Qt.Key_AudioRepeat
	CapsLock                          = PYQT.Qt.Key_CapsLock
	Aring                             = PYQT.Qt.Key_Aring
	PageDown                          = PYQT.Qt.Key_PageDown
	Calendar                          = PYQT.Qt.Key_Calendar
	ContrastAdjust                    = PYQT.Qt.Key_ContrastAdjust
	AudioCycleTrack                   = PYQT.Qt.Key_AudioCycleTrack
	Meeting                           = PYQT.Qt.Key_Meeting
	Terminal                          = PYQT.Qt.Key_Terminal
	threequarters                     = PYQT.Qt.Key_threequarters
	copyright                         = PYQT.Qt.Key_copyright
	unknown                           = PYQT.Qt.Key_unknown
	Asterisk                          = PYQT.Qt.Key_Asterisk
	iTouch                            = PYQT.Qt.Key_iTouch
	Eacute                            = PYQT.Qt.Key_Eacute
	periodcentered                    = PYQT.Qt.Key_periodcentered
	Camera                            = PYQT.Qt.Key_Camera
	Flip                              = PYQT.Qt.Key_Flip
	MediaNext                         = PYQT.Qt.Key_MediaNext
	Search                            = PYQT.Qt.Key_Search
	Kana_Shift                        = PYQT.Qt.Key_Kana_Shift
	Igrave                            = PYQT.Qt.Key_Igrave
	Battery                           = PYQT.Qt.Key_Battery
	Henkan                            = PYQT.Qt.Key_Henkan
	Tools                             = PYQT.Qt.Key_Tools
	Cancel                            = PYQT.Qt.Key_Cancel
	Hangul_PostHanja                  = PYQT.Qt.Key_Hangul_PostHanja
	Any                               = PYQT.Qt.Key_Any
	Hangul                            = PYQT.Qt.Key_Hangul
	Ucircumflex                       = PYQT.Qt.Key_Ucircumflex
	Hangup                            = PYQT.Qt.Key_Hangup
	ZoomOut                           = PYQT.Qt.Key_ZoomOut
	AddFavorite                       = PYQT.Qt.Key_AddFavorite
	Num_5                             = PYQT.Qt.Key_5
	Num_4                             = PYQT.Qt.Key_4
	Num_7                             = PYQT.Qt.Key_7
	Num_6                             = PYQT.Qt.Key_6
	Num_1                             = PYQT.Qt.Key_1
	Num_0                             = PYQT.Qt.Key_0
	Num_3                             = PYQT.Qt.Key_3
	Num_2                             = PYQT.Qt.Key_2
	Dead_Iota                         = PYQT.Qt.Key_Dead_Iota
	Num_9                             = PYQT.Qt.Key_9
	Num_8                             = PYQT.Qt.Key_8
	E                                 = PYQT.Qt.Key_E
	D                                 = PYQT.Qt.Key_D
	G                                 = PYQT.Qt.Key_G
	F                                 = PYQT.Qt.Key_F
	A                                 = PYQT.Qt.Key_A
	division                          = PYQT.Qt.Key_division
	C                                 = PYQT.Qt.Key_C
	B                                 = PYQT.Qt.Key_B
	M                                 = PYQT.Qt.Key_M
	L                                 = PYQT.Qt.Key_L
	O                                 = PYQT.Qt.Key_O
	N                                 = PYQT.Qt.Key_N
	I                                 = PYQT.Qt.Key_I
	Semicolon                         = PYQT.Qt.Key_Semicolon
	K                                 = PYQT.Qt.Key_K
	J                                 = PYQT.Qt.Key_J
	U                                 = PYQT.Qt.Key_U
	T                                 = PYQT.Qt.Key_T
	W                                 = PYQT.Qt.Key_W
	V                                 = PYQT.Qt.Key_V
	MediaRecord                       = PYQT.Qt.Key_MediaRecord
	P                                 = PYQT.Qt.Key_P
	S                                 = PYQT.Qt.Key_S
	R                                 = PYQT.Qt.Key_R
	Y                                 = PYQT.Qt.Key_Y
	X                                 = PYQT.Qt.Key_X
	Z                                 = PYQT.Qt.Key_Z
	F4                                = PYQT.Qt.Key_F4
	F5                                = PYQT.Qt.Key_F5
	F6                                = PYQT.Qt.Key_F6
	F7                                = PYQT.Qt.Key_F7
	F1                                = PYQT.Qt.Key_F1
	F2                                = PYQT.Qt.Key_F2
	F3                                = PYQT.Qt.Key_F3
	F8                                = PYQT.Qt.Key_F8
	F9                                = PYQT.Qt.Key_F9
	Odiaeresis                        = PYQT.Qt.Key_Odiaeresis
	Escape                            = PYQT.Qt.Key_Escape
	ydiaeresis                        = PYQT.Qt.Key_ydiaeresis
	Meta                              = PYQT.Qt.Key_Meta
	Support                           = PYQT.Qt.Key_Support
	Documents                         = PYQT.Qt.Key_Documents
	Egrave                            = PYQT.Qt.Key_Egrave
	nobreakspace                      = PYQT.Qt.Key_nobreakspace
	PowerOff                          = PYQT.Qt.Key_PowerOff
	Explorer                          = PYQT.Qt.Key_Explorer
	RotateWindows                     = PYQT.Qt.Key_RotateWindows
	MonBrightnessDown                 = PYQT.Qt.Key_MonBrightnessDown
	degree                            = PYQT.Qt.Key_degree
	View                              = PYQT.Qt.Key_View
	BraceLeft                         = PYQT.Qt.Key_BraceLeft
	Reload                            = PYQT.Qt.Key_Reload
	threesuperior                     = PYQT.Qt.Key_threesuperior
	mu                                = PYQT.Qt.Key_mu
	SysReq                            = PYQT.Qt.Key_SysReq
	Menu                              = PYQT.Qt.Key_Menu
	WLAN                              = PYQT.Qt.Key_WLAN
	Dead_Hook                         = PYQT.Qt.Key_Dead_Hook
	Slash                             = PYQT.Qt.Key_Slash
	ParenLeft                         = PYQT.Qt.Key_ParenLeft
	Iacute                            = PYQT.Qt.Key_Iacute
	News                              = PYQT.Qt.Key_News
	LogOff                            = PYQT.Qt.Key_LogOff
	onehalf                           = PYQT.Qt.Key_onehalf
	Clear                             = PYQT.Qt.Key_Clear
	Word                              = PYQT.Qt.Key_Word
	Udiaeresis                        = PYQT.Qt.Key_Udiaeresis
	Romaji                            = PYQT.Qt.Key_Romaji
	Time                              = PYQT.Qt.Key_Time
	onesuperior                       = PYQT.Qt.Key_onesuperior
	MediaStop                         = PYQT.Qt.Key_MediaStop
	Bluetooth                         = PYQT.Qt.Key_Bluetooth
	Ocircumflex                       = PYQT.Qt.Key_Ocircumflex
	Right                             = PYQT.Qt.Key_Right
	paragraph                         = PYQT.Qt.Key_paragraph
	Down                              = PYQT.Qt.Key_Down
	Dead_Cedilla                      = PYQT.Qt.Key_Dead_Cedilla
	QuoteDbl                          = PYQT.Qt.Key_QuoteDbl
	Backspace                         = PYQT.Qt.Key_Backspace
	ZoomIn                            = PYQT.Qt.Key_ZoomIn
	Reply                             = PYQT.Qt.Key_Reply
	Dead_Ogonek                       = PYQT.Qt.Key_Dead_Ogonek
	Music                             = PYQT.Qt.Key_Music
	Yacute                            = PYQT.Qt.Key_Yacute
	Atilde                            = PYQT.Qt.Key_Atilde
	ETH                               = PYQT.Qt.Key_ETH
	Ecircumflex                       = PYQT.Qt.Key_Ecircumflex
	PageUp                            = PYQT.Qt.Key_PageUp
	Hiragana_Katakana                 = PYQT.Qt.Key_Hiragana_Katakana
	CD                                = PYQT.Qt.Key_CD
	cedilla                           = PYQT.Qt.Key_cedilla
	Execute                           = PYQT.Qt.Key_Execute
	F18                               = PYQT.Qt.Key_F18
	F19                               = PYQT.Qt.Key_F19
	F16                               = PYQT.Qt.Key_F16
	F17                               = PYQT.Qt.Key_F17
	F14                               = PYQT.Qt.Key_F14
	F15                               = PYQT.Qt.Key_F15
	F12                               = PYQT.Qt.Key_F12
	F13                               = PYQT.Qt.Key_F13
	F10                               = PYQT.Qt.Key_F10
	F11                               = PYQT.Qt.Key_F11
	Back                              = PYQT.Qt.Key_Back
	Memo                              = PYQT.Qt.Key_Memo
	Control                           = PYQT.Qt.Key_Control
	No                                = PYQT.Qt.Key_No
	ordfeminine                       = PYQT.Qt.Key_ordfeminine
	Ampersand                         = PYQT.Qt.Key_Ampersand
	currency                          = PYQT.Qt.Key_currency
	Book                              = PYQT.Qt.Key_Book
	BracketRight                      = PYQT.Qt.Key_BracketRight
	MonBrightnessUp                   = PYQT.Qt.Key_MonBrightnessUp
	Dead_Doubleacute                  = PYQT.Qt.Key_Dead_Doubleacute
	MultipleCandidate                 = PYQT.Qt.Key_MultipleCandidate
	TopMenu                           = PYQT.Qt.Key_TopMenu
	Touroku                           = PYQT.Qt.Key_Touroku
	Massyo                            = PYQT.Qt.Key_Massyo
	Up                                = PYQT.Qt.Key_Up
	MediaLast                         = PYQT.Qt.Key_MediaLast
	Hangul_End                        = PYQT.Qt.Key_Hangul_End
	Plus                              = PYQT.Qt.Key_Plus
	AsciiCircum                       = PYQT.Qt.Key_AsciiCircum
	MediaPlay                         = PYQT.Qt.Key_MediaPlay
	Help                              = PYQT.Qt.Key_Help
	Tab                               = PYQT.Qt.Key_Tab
	Percent                           = PYQT.Qt.Key_Percent
	brokenbar                         = PYQT.Qt.Key_brokenbar
	Direction_R                       = PYQT.Qt.Key_Direction_R
	Print                             = PYQT.Qt.Key_Print
	Direction_L                       = PYQT.Qt.Key_Direction_L
	RotationKB                        = PYQT.Qt.Key_RotationKB
	Aacute                            = PYQT.Qt.Key_Aacute
	Spell                             = PYQT.Qt.Key_Spell
	ToDoList                          = PYQT.Qt.Key_ToDoList
	SplitScreen                       = PYQT.Qt.Key_SplitScreen
	diaeresis                         = PYQT.Qt.Key_diaeresis
	PreviousCandidate                 = PYQT.Qt.Key_PreviousCandidate
	Home                              = PYQT.Qt.Key_Home
	Hyper_L                           = PYQT.Qt.Key_Hyper_L
	Dead_Abovedot                     = PYQT.Qt.Key_Dead_Abovedot
	THORN                             = PYQT.Qt.Key_THORN
	BackForward                       = PYQT.Qt.Key_BackForward
	Delete                            = PYQT.Qt.Key_Delete
	registered                        = PYQT.Qt.Key_registered
	Hyper_R                           = PYQT.Qt.Key_Hyper_R
	Dead_Circumflex                   = PYQT.Qt.Key_Dead_Circumflex
	MediaPrevious                     = PYQT.Qt.Key_MediaPrevious
	ToggleCallHangup                  = PYQT.Qt.Key_ToggleCallHangup
	ssharp                            = PYQT.Qt.Key_ssharp
	AudioRandomPlay                   = PYQT.Qt.Key_AudioRandomPlay
	Mode_switch                       = PYQT.Qt.Key_Mode_switch
	Close                             = PYQT.Qt.Key_Close
	guillemotleft                     = PYQT.Qt.Key_guillemotleft
	Q                                 = PYQT.Qt.Key_Q
	Go                                = PYQT.Qt.Key_Go
########################################################################
class LayoutDirection:
	RightToLeft                       = PYQT.Qt.RightToLeft
	LayoutDirectionAuto               = PYQT.Qt.LayoutDirectionAuto
	LeftToRight                       = PYQT.Qt.LeftToRight
########################################################################
class MouseButton:
	RightButton                       = PYQT.Qt.RightButton
	MiddleButton                      = PYQT.Qt.MiddleButton
	NoButton                          = PYQT.Qt.NoButton
	LeftButton                        = PYQT.Qt.LeftButton
	MouseButtonMask                   = PYQT.Qt.MouseButtonMask
	XButton1                          = PYQT.Qt.XButton1
	XButton2                          = PYQT.Qt.XButton2
	MidButton                         = PYQT.Qt.MidButton
########################################################################
class Orientation:
	Horizontal                        = PYQT.Qt.Horizontal
	Vertical                          = PYQT.Qt.Vertical
########################################################################
class PenCapStyle:
	FlatCap                           = PYQT.Qt.FlatCap
	RoundCap                          = PYQT.Qt.RoundCap
	SquareCap                         = PYQT.Qt.SquareCap
	MPenCapStyle                      = PYQT.Qt.MPenCapStyle
########################################################################
class PenJoinStyle:
	RoundJoin                         = PYQT.Qt.RoundJoin
	MiterJoin                         = PYQT.Qt.MiterJoin
	MPenJoinStyle                     = PYQT.Qt.MPenJoinStyle
	BevelJoin                         = PYQT.Qt.BevelJoin
	SvgMiterJoin                      = PYQT.Qt.SvgMiterJoin
########################################################################
class ScrollBarPolicy:
	AsNeeded                          = PYQT.Qt.ScrollBarAsNeeded
	AlwaysOff                         = PYQT.Qt.ScrollBarAlwaysOff
	AlwaysOn                          = PYQT.Qt.ScrollBarAlwaysOn
########################################################################
class SizeHint:
	MinimumDescent                    = PYQT.Qt.MinimumDescent
	PreferredSize                     = PYQT.Qt.PreferredSize
	MinimumSize                       = PYQT.Qt.MinimumSize
	MaximumSize                       = PYQT.Qt.MaximumSize
########################################################################
class SizeMode:
	AbsoluteSize                      = PYQT.Qt.AbsoluteSize
	RelativeSize                      = PYQT.Qt.RelativeSize
########################################################################
class SortOrder:
	Ascending                         = PYQT.Qt.AscendingOrder
	Descending                        = PYQT.Qt.DescendingOrder
########################################################################
class TextFormat:
	PlainText                         = PYQT.Qt.PlainText
	AutoText                          = PYQT.Qt.AutoText
	# LogText   = PYQT.Qt.LogText
	RichText                          = PYQT.Qt.RichText
########################################################################
class TextInteractionFlag:
	TextEditable                      = PYQT.Qt.TextEditable
	TextSelectableByKeyboard          = PYQT.Qt.TextSelectableByKeyboard
	NoTextInteraction                 = PYQT.Qt.NoTextInteraction
	TextSelectableByMouse             = PYQT.Qt.TextSelectableByMouse
	TextBrowserInteraction            = PYQT.Qt.TextBrowserInteraction
	LinksAccessibleByKeyboard         = PYQT.Qt.LinksAccessibleByKeyboard
	LinksAccessibleByMouse            = PYQT.Qt.LinksAccessibleByMouse
	TextEditorInteraction             = PYQT.Qt.TextEditorInteraction
########################################################################
class TileRule:
	StretchTile                       = PYQT.Qt.StretchTile
	RepeatTile                        = PYQT.Qt.RepeatTile
	RoundTile                         = PYQT.Qt.RoundTile
########################################################################
class TimeSpec:
	OffsetFromUTC                     = PYQT.Qt.OffsetFromUTC
	UTC                               = PYQT.Qt.UTC
	LocalTime                         = PYQT.Qt.LocalTime
########################################################################
class ToolBarArea:
	RightToolBarArea                  = PYQT.Qt.RightToolBarArea
	TopToolBarArea                    = PYQT.Qt.TopToolBarArea
	ToolBarArea_Mask                  = PYQT.Qt.ToolBarArea_Mask
	NoToolBarArea                     = PYQT.Qt.NoToolBarArea
	LeftToolBarArea                   = PYQT.Qt.LeftToolBarArea
	AllToolBarAreas                   = PYQT.Qt.AllToolBarAreas
	BottomToolBarArea                 = PYQT.Qt.BottomToolBarArea
########################################################################
class ToolButtonStyle:
	ToolButtonIconOnly                = PYQT.Qt.ToolButtonIconOnly
	ToolButtonTextBesideIcon          = PYQT.Qt.ToolButtonTextBesideIcon
	ToolButtonTextOnly                = PYQT.Qt.ToolButtonTextOnly
	ToolButtonFollowStyle             = PYQT.Qt.ToolButtonFollowStyle
	ToolButtonTextUnderIcon           = PYQT.Qt.ToolButtonTextUnderIcon
########################################################################
class TouchPointState:
	TouchPointReleased                = PYQT.Qt.TouchPointReleased
	TouchPointPressed                 = PYQT.Qt.TouchPointPressed
	TouchPointMoved                   = PYQT.Qt.TouchPointMoved
	TouchPointStationary              = PYQT.Qt.TouchPointStationary
########################################################################
class UIEffect:
	AnimateCombo                      = PYQT.Qt.UI_AnimateCombo
	FadeMenu                          = PYQT.Qt.UI_FadeMenu
	AnimateTooltip                    = PYQT.Qt.UI_AnimateTooltip
	AnimateMenu                       = PYQT.Qt.UI_AnimateMenu
	FadeTooltip                       = PYQT.Qt.UI_FadeTooltip
	General                           = PYQT.Qt.UI_General
	AnimateToolBox                    = PYQT.Qt.UI_AnimateToolBox
########################################################################
class WhiteSpaceMode:
	WhiteSpaceNoWrap                  = PYQT.Qt.WhiteSpaceNoWrap
	WhiteSpaceModeUndefined           = PYQT.Qt.WhiteSpaceModeUndefined
	WhiteSpaceNormal                  = PYQT.Qt.WhiteSpaceNormal
	WhiteSpacePre                     = PYQT.Qt.WhiteSpacePre
########################################################################
class WidgetAttribute:
	CustomWhatsThis                   = PYQT.Qt.WA_CustomWhatsThis
	SetFont                           = PYQT.Qt.WA_SetFont
	NoChildEventsForParent            = PYQT.Qt.WA_NoChildEventsForParent
	AlwaysShowToolTips                = PYQT.Qt.WA_AlwaysShowToolTips
	MacBrushedMetal                   = PYQT.Qt.WA_MacBrushedMetal
	AcceptTouchEvents                 = PYQT.Qt.WA_AcceptTouchEvents
	X11NetWmWindowTypeUtility         = PYQT.Qt.WA_X11NetWmWindowTypeUtility
	Hover                             = PYQT.Qt.WA_Hover
	TransparentForMouseEvents         = PYQT.Qt.WA_TransparentForMouseEvents
	PendingUpdate                     = PYQT.Qt.WA_PendingUpdate
	PaintUnclipped                    = PYQT.Qt.WA_PaintUnclipped
	MacMiniSize                       = PYQT.Qt.WA_MacMiniSize
	MacOpaqueSizeGrip                 = PYQT.Qt.WA_MacOpaqueSizeGrip
	X11NetWmWindowTypeDropDownMenu    = PYQT.Qt.WA_X11NetWmWindowTypeDropDownMenu
	SetLayoutDirection                = PYQT.Qt.WA_SetLayoutDirection
	NoMousePropagation                = PYQT.Qt.WA_NoMousePropagation
	SetLocale                         = PYQT.Qt.WA_SetLocale
	QuitOnClose                       = PYQT.Qt.WA_QuitOnClose
	MacSmallSize                      = PYQT.Qt.WA_MacSmallSize
	MSWindowsUseDirect3D              = PYQT.Qt.WA_MSWindowsUseDirect3D
	TouchPadAcceptSingleTouchEvents   = PYQT.Qt.WA_TouchPadAcceptSingleTouchEvents
	WState_Reparented                 = PYQT.Qt.WA_WState_Reparented
	ForceUpdatesDisabled              = PYQT.Qt.WA_ForceUpdatesDisabled
	X11NetWmWindowTypeDND             = PYQT.Qt.WA_X11NetWmWindowTypeDND
	MacVariableSize                   = PYQT.Qt.WA_MacVariableSize
	LayoutUsesWidgetRect              = PYQT.Qt.WA_LayoutUsesWidgetRect
	SetStyle                          = PYQT.Qt.WA_SetStyle
	WState_ConfigPending              = PYQT.Qt.WA_WState_ConfigPending
	X11NetWmWindowTypeDesktop         = PYQT.Qt.WA_X11NetWmWindowTypeDesktop
	X11NetWmWindowTypeMenu            = PYQT.Qt.WA_X11NetWmWindowTypeMenu
	MacShowFocusRect                  = PYQT.Qt.WA_MacShowFocusRect
	NoMouseReplay                     = PYQT.Qt.WA_NoMouseReplay
	X11NetWmWindowTypeDock            = PYQT.Qt.WA_X11NetWmWindowTypeDock
	SetPalette                        = PYQT.Qt.WA_SetPalette
	OpaquePaintEvent                  = PYQT.Qt.WA_OpaquePaintEvent
	UpdatesDisabled                   = PYQT.Qt.WA_UpdatesDisabled
	MouseTracking                     = PYQT.Qt.WA_MouseTracking
	WState_Created                    = PYQT.Qt.WA_WState_Created
	NoSystemBackground                = PYQT.Qt.WA_NoSystemBackground
	Disabled                          = PYQT.Qt.WA_Disabled
	InvalidSize                       = PYQT.Qt.WA_InvalidSize
	WState_InPaintEvent               = PYQT.Qt.WA_WState_InPaintEvent
	MacMetalStyle                     = PYQT.Qt.WA_MacMetalStyle
	X11NetWmWindowTypePopupMenu       = PYQT.Qt.WA_X11NetWmWindowTypePopupMenu
	NativeWindow                      = PYQT.Qt.WA_NativeWindow
	WState_ExplicitShowHide           = PYQT.Qt.WA_WState_ExplicitShowHide
	OutsideWSRange                    = PYQT.Qt.WA_OutsideWSRange
	SetCursor                         = PYQT.Qt.WA_SetCursor
	# MergeSoftkeys                   = PYQT.Qt.WA_MergeSoftkeys
	SetWindowIcon                     = PYQT.Qt.WA_SetWindowIcon
	X11DoNotAcceptFocus               = PYQT.Qt.WA_X11DoNotAcceptFocus
	StyledBackground                  = PYQT.Qt.WA_StyledBackground
	X11NetWmWindowTypeToolBar         = PYQT.Qt.WA_X11NetWmWindowTypeToolBar
	KeyCompression                    = PYQT.Qt.WA_KeyCompression
	InputMethodTransparent            = PYQT.Qt.WA_InputMethodTransparent
	X11NetWmWindowTypeToolTip         = PYQT.Qt.WA_X11NetWmWindowTypeToolTip
	X11NetWmWindowTypeSplash          = PYQT.Qt.WA_X11NetWmWindowTypeSplash
	InputMethodEnabled                = PYQT.Qt.WA_InputMethodEnabled
	StaticContents                    = PYQT.Qt.WA_StaticContents
	NoX11EventCompression             = PYQT.Qt.WA_NoX11EventCompression
	AcceptDrops                       = PYQT.Qt.WA_AcceptDrops
	TintedBackground                  = PYQT.Qt.WA_TintedBackground
	Mapped                            = PYQT.Qt.WA_Mapped
	MouseNoMask                       = PYQT.Qt.WA_MouseNoMask
	TranslucentBackground             = PYQT.Qt.WA_TranslucentBackground
	KeyboardFocusChange               = PYQT.Qt.WA_KeyboardFocusChange
	X11NetWmWindowTypeNotification    = PYQT.Qt.WA_X11NetWmWindowTypeNotification
	LaidOut                           = PYQT.Qt.WA_LaidOut
	WState_OwnSizePolicy              = PYQT.Qt.WA_WState_OwnSizePolicy
	MacFrameworkScaled                = PYQT.Qt.WA_MacFrameworkScaled
	MacNoClickThrough                 = PYQT.Qt.WA_MacNoClickThrough
	X11OpenGLOverlay                  = PYQT.Qt.WA_X11OpenGLOverlay
	AttributeCount                    = PYQT.Qt.WA_AttributeCount
	PaintOnScreen                     = PYQT.Qt.WA_PaintOnScreen
	X11NetWmWindowTypeCombo           = PYQT.Qt.WA_X11NetWmWindowTypeCombo
	PendingResizeEvent                = PYQT.Qt.WA_PendingResizeEvent
	MacAlwaysShowToolWindow           = PYQT.Qt.WA_MacAlwaysShowToolWindow
	ShowWithoutActivating             = PYQT.Qt.WA_ShowWithoutActivating
	# MergeSoftkeysRecursively        = PYQT.Qt.WA_MergeSoftkeysRecursively
	WState_CompressKeys               = PYQT.Qt.WA_WState_CompressKeys
	UnderMouse                        = PYQT.Qt.WA_UnderMouse
	WState_Visible                    = PYQT.Qt.WA_WState_Visible
	GroupLeader                       = PYQT.Qt.WA_GroupLeader
	MacNormalSize                     = PYQT.Qt.WA_MacNormalSize
	LayoutOnEntireRect                = PYQT.Qt.WA_LayoutOnEntireRect
	DeleteOnClose                     = PYQT.Qt.WA_DeleteOnClose
	WindowPropagation                 = PYQT.Qt.WA_WindowPropagation
	Moved                             = PYQT.Qt.WA_Moved
	# PaintOutsidePaintEvent          = PYQT.Qt.WA_PaintOutsidePaintEvent
	DontCreateNativeAncestors         = PYQT.Qt.WA_DontCreateNativeAncestors
	Resized                           = PYQT.Qt.WA_Resized
	PendingMoveEvent                  = PYQT.Qt.WA_PendingMoveEvent
	StyleSheet                        = PYQT.Qt.WA_StyleSheet
	WState_Hidden                     = PYQT.Qt.WA_WState_Hidden
	X11NetWmWindowTypeDialog          = PYQT.Qt.WA_X11NetWmWindowTypeDialog
	ForceDisabled                     = PYQT.Qt.WA_ForceDisabled
	NoChildEventsFromChildren         = PYQT.Qt.WA_NoChildEventsFromChildren
	WState_Polished                   = PYQT.Qt.WA_WState_Polished
	WindowModified                    = PYQT.Qt.WA_WindowModified
########################################################################
class WindowFrameSection:
	TopRightSection                   = PYQT.Qt.TopRightSection
	BottomRightSection                = PYQT.Qt.BottomRightSection
	NoSection                         = PYQT.Qt.NoSection
	TopSection                        = PYQT.Qt.TopSection
	TopLeftSection                    = PYQT.Qt.TopLeftSection
	RightSection                      = PYQT.Qt.RightSection
	BottomLeftSection                 = PYQT.Qt.BottomLeftSection
	TitleBarArea                      = PYQT.Qt.TitleBarArea
	LeftSection                       = PYQT.Qt.LeftSection
	BottomSection                     = PYQT.Qt.BottomSection
########################################################################
class WindowState:
	WindowNoState                     = PYQT.Qt.WindowNoState
	WindowFullScreen                  = PYQT.Qt.WindowFullScreen
	WindowMaximized                   = PYQT.Qt.WindowMaximized
	WindowActive                      = PYQT.Qt.WindowActive
	WindowMinimized                   = PYQT.Qt.WindowMinimized
########################################################################
class WindowType:
	SubWindow                         = PYQT.Qt.SubWindow
	Sheet                             = PYQT.Qt.Sheet
	Desktop                           = PYQT.Qt.Desktop
	WindowType_Mask                   = PYQT.Qt.WindowType_Mask
	WindowShadeButtonHint             = PYQT.Qt.WindowShadeButtonHint
	Window                            = PYQT.Qt.Window
	WindowMinimizeButtonHint          = PYQT.Qt.WindowMinimizeButtonHint
	# WindowSoftkeysVisibleHint    = PYQT.Qt.WindowSoftkeysVisibleHint
	CustomizeWindowHint               = PYQT.Qt.CustomizeWindowHint
	WindowCancelButtonHint            = PYQT.Qt.WindowCancelButtonHint
	WindowMaximizeButtonHint          = PYQT.Qt.WindowMaximizeButtonHint
	Widget                            = PYQT.Qt.Widget
	Popup                             = PYQT.Qt.Popup
	WindowStaysOnTopHint              = PYQT.Qt.WindowStaysOnTopHint
	BypassGraphicsProxyWidget         = PYQT.Qt.BypassGraphicsProxyWidget
	Tool                              = PYQT.Qt.Tool
	WindowTitleHint                   = PYQT.Qt.WindowTitleHint
	X11BypassWindowManagerHint        = PYQT.Qt.X11BypassWindowManagerHint
	MSWindowsFixedSizeDialogHint      = PYQT.Qt.MSWindowsFixedSizeDialogHint
	WindowMinMaxButtonsHint           = PYQT.Qt.WindowMinMaxButtonsHint
	MacWindowToolBarButtonHint        = PYQT.Qt.MacWindowToolBarButtonHint
	FramelessWindowHint               = PYQT.Qt.FramelessWindowHint
	WindowOkButtonHint                = PYQT.Qt.WindowOkButtonHint
	MSWindowsOwnDC                    = PYQT.Qt.MSWindowsOwnDC
	WindowCloseButtonHint             = PYQT.Qt.WindowCloseButtonHint
	Dialog                            = PYQT.Qt.Dialog
	# WindowSoftkeysRespondHint    = PYQT.Qt.WindowSoftkeysRespondHint
	WindowSystemMenuHint              = PYQT.Qt.WindowSystemMenuHint
	ToolTip                           = PYQT.Qt.ToolTip
	WindowContextHelpButtonHint       = PYQT.Qt.WindowContextHelpButtonHint
	Drawer                            = PYQT.Qt.Drawer
	WindowStaysOnBottomHint           = PYQT.Qt.WindowStaysOnBottomHint
	SplashScreen                      = PYQT.Qt.SplashScreen

########################################################################
class Font:
	""""""
	class SpacingType:
		PercentageSpacing = PYQT.QFont.PercentageSpacing # A value of 100 will keep the spacing unchanged; a value of 200 will enlarge the spacing after a character by the width of the character itself.
		AbsoluteSpacing   = PYQT.QFont.AbsoluteSpacing   # A positive value increases the letter spacing by the corresponding pixels; a negative value decreases the spacing.
	class StyleHint:
		AnyStyle   = PYQT.QFont.AnyStyle    # leaves the font matching algorithm to choose the family. This is the default.
		SansSerif  = PYQT.QFont.SansSerif   # the font matcher prefer sans serif fonts.
		Helvetica  = PYQT.QFont.Helvetica   # is a synonym for SansSerif.
		Serif      = PYQT.QFont.Serif       # the font matcher prefers serif fonts.
		Times      = PYQT.QFont.Times       # is a synonym for Serif.
		TypeWriter = PYQT.QFont.TypeWriter  # the font matcher prefers fixed pitch fonts.
		Courier    = PYQT.QFont.Courier     # a synonym for TypeWriter.
		OldEnglish = PYQT.QFont.OldEnglish  # the font matcher prefers decorative fonts.
		Decorative = PYQT.QFont.Decorative  # is a synonym for OldEnglish.
		Monospace  = PYQT.QFont.Monospace   # the font matcher prefers fonts that map to the CSS generic font-family monospace.
		Fantasy    = PYQT.QFont.Fantasy     # the font matcher prefers fonts that map to the CSS generic font-family fantasy.
		Cursive    = PYQT.QFont.Cursive     # the font matcher prefers fonts that map to the CSS generic font-family cursive.
		System     = PYQT.QFont.System      # the font matcher prefers system fonts.
	class Weight:
		Light    = PYQT.QFont.Light    # 25
		Normal   = PYQT.QFont.Normal   # 50
		DemiBold = PYQT.QFont.DemiBold # 63
		Bold     = PYQT.QFont.Bold     # 75
		Black    = PYQT.QFont.Black    # 87

	class Capitalization:
		MixedCase    = PYQT.QFont.MixedCase    # This is the normal text rendering option where no capitalization change is applied.
		AllUppercase = PYQT.QFont.AllUppercase # This alters the text to be rendered in all uppercase type.
		AllLowercase = PYQT.QFont.AllLowercase # This alters the text to be rendered in all lowercase type.
		SmallCaps    = PYQT.QFont.SmallCaps    # This alters the text to be rendered in small-caps type.
		Capitalize   = PYQT.QFont.Capitalize   # This alters the text to be rendered with the first character of each word as an uppercase character.
		
	class Stretch:
		UltraCondensed = PYQT.QFont.UltraCondensed # 50
		ExtraCondensed = PYQT.QFont.ExtraCondensed # 62
		Condensed      = PYQT.QFont.Condensed      # 75
		SemiCondensed  = PYQT.QFont.SemiCondensed  # 87
		Unstretched    = PYQT.QFont.Unstretched    # 100
		SemiExpanded   = PYQT.QFont.SemiExpanded   # 112
		Expanded       = PYQT.QFont.Expanded       # 125
		ExtraExpanded  = PYQT.QFont.ExtraExpanded  # 150
		UltraExpanded  = PYQT.QFont.UltraExpanded  # 200
########################################################################
class AbstractItemView:
	########################################################################
	class Drag_Drop_Mode:
		DragDrop     = PYQT.QAbstractItemView.DragDrop
		DragOnly     = PYQT.QAbstractItemView.DragOnly
		DropOnly     = PYQT.QAbstractItemView.DropOnly
		InternalMove = PYQT.QAbstractItemView.InternalMove
		NoDragDrop   = PYQT.QAbstractItemView.NoDragDrop
	########################################################################
	class CursorAction:
		Down     = PYQT.QAbstractItemView.MoveDown
		Up       = PYQT.QAbstractItemView.MoveUp
		Left     = PYQT.QAbstractItemView.MoveLeft
		Right    = PYQT.QAbstractItemView.MoveRight
		Home     = PYQT.QAbstractItemView.MoveHome
		End      = PYQT.QAbstractItemView.MoveEnd
		Next     = PYQT.QAbstractItemView.MoveNext
		Previous = PYQT.QAbstractItemView.MovePrevious
		PageUp   = PYQT.QAbstractItemView.MovePageUp
		PageDown = PYQT.QAbstractItemView.MovePageDown
	########################################################################
	class DropIndicatorPosition:
		AboveItem  = PYQT.QAbstractItemView.AboveItem
		BelowItem  = PYQT.QAbstractItemView.BelowItem
		OnItem     = PYQT.QAbstractItemView.OnItem
		OnViewport = PYQT.QAbstractItemView.OnViewport
	########################################################################
	class EditTrigger:
		AllEditTriggers = PYQT.QAbstractItemView.AllEditTriggers
		AnyKeyPressed   = PYQT.QAbstractItemView.AnyKeyPressed
		CurrentChanged  = PYQT.QAbstractItemView.CurrentChanged
		DoubleClicked   = PYQT.QAbstractItemView.DoubleClicked
		EditKeyPressed  = PYQT.QAbstractItemView.EditKeyPressed
		NoEditTriggers  = PYQT.QAbstractItemView.NoEditTriggers
		SelectedClicked = PYQT.QAbstractItemView.SelectedClicked
	########################################################################
	class ScrollHint:
		EnsureVisible    = PYQT.QAbstractItemView.EnsureVisible
		PositionAtBottom = PYQT.QAbstractItemView.PositionAtBottom
		PositionAtCenter = PYQT.QAbstractItemView.PositionAtCenter
		PositionAtTop    = PYQT.QAbstractItemView.PositionAtTop
	########################################################################
	class ScrollMode:
		PerItem  = PYQT.QAbstractItemView.ScrollPerItem
		PerPixel = PYQT.QAbstractItemView.ScrollPerPixel
	########################################################################
	class SelectionBehavior:
		Columns = PYQT.QAbstractItemView.SelectColumns
		Items   = PYQT.QAbstractItemView.SelectItems
		Rows    = PYQT.QAbstractItemView.SelectRows
	########################################################################
	class SelectionMode:
		Contiguous = PYQT.QAbstractItemView.ContiguousSelection
		Extended   = PYQT.QAbstractItemView.ExtendedSelection
		Multi      = PYQT.QAbstractItemView.MultiSelection
		No         = PYQT.QAbstractItemView.NoSelection
		Single     = PYQT.QAbstractItemView.SingleSelection
	########################################################################
	class Shadow:
		Plain  = PYQT.QAbstractItemView.Plain
		Raised = PYQT.QAbstractItemView.Raised
		Sunken = PYQT.QAbstractItemView.Sunken
	########################################################################	
	class Shape:
		Box         = PYQT.QAbstractItemView.Box
		HLine       = PYQT.QAbstractItemView.HLine
		NoFrame     = PYQT.QAbstractItemView.NoFrame
		Panel       = PYQT.QAbstractItemView.Panel
		StyledPanel = PYQT.QAbstractItemView.StyledPanel
		VLine       = PYQT.QAbstractItemView.VLine
		WinPanel    = PYQT.QAbstractItemView.WinPanel
	########################################################################
	class State:
		Animating     = PYQT.QAbstractItemView.AnimatingState
		Collapsing    = PYQT.QAbstractItemView.CollapsingState
		DragSelecting = PYQT.QAbstractItemView.DragSelectingState
		Dragging      = PYQT.QAbstractItemView.DraggingState
		Editing       = PYQT.QAbstractItemView.EditingState
		Expanding     = PYQT.QAbstractItemView.ExpandingState
		No            = PYQT.QAbstractItemView.NoState

########################################################################
class PenStyles:
	NoPen                        = PYQT.Qt.NoPen          # no line at all. For example, QPainter.drawRect() fills but does not draw any boundary line.
	SolidLine                    = PYQT.Qt.SolidLine      # A plain line.
	DashLine                     = PYQT.Qt.DashLine       # Dashes separated by a few pixels.
	DotLine                      = PYQT.Qt.DotLine        # Dots separated by a few pixels.
	DashDotLine                  = PYQT.Qt.DashDotLine    # Alternate dots and dashes.
	DashDotDotLine               = PYQT.Qt.DashDotDotLine # One dash, two dots, one dash, two dots.
	CustomDashLine               = PYQT.Qt.CustomDashLine # A custom pattern defined using QPainterPathStroker.setDashPattern() .
########################################################################
class BrushStyles:
	NoBrush                      = PYQT.Qt.NoBrush                # No brush pattern.
	SolidPattern                 = PYQT.Qt.SolidPattern           # Uniform color.
	Dense1Pattern                = PYQT.Qt.Dense1Pattern          # Extremely dense brush pattern.
	Dense2Pattern                = PYQT.Qt.Dense2Pattern          # Very dense brush pattern.
	Dense3Pattern                = PYQT.Qt.Dense3Pattern          # Somewhat dense brush pattern.
	Dense4Pattern                = PYQT.Qt.Dense4Pattern          # Half dense brush pattern.
	Dense5Pattern                = PYQT.Qt.Dense5Pattern          # Somewhat sparse brush pattern.
	Dense6Pattern                = PYQT.Qt.Dense6Pattern          # Very sparse brush pattern.
	Dense7Pattern                = PYQT.Qt.Dense7Pattern          # Extremely sparse brush pattern.
	HorPattern                   = PYQT.Qt.HorPattern             # Horizontal lines.
	VerPattern                   = PYQT.Qt.VerPattern             # Vertical lines.
	CrossPattern                 = PYQT.Qt.CrossPattern           # Crossing horizontal and vertical lines.
	BDiagPattern                 = PYQT.Qt.BDiagPattern           # Backward diagonal lines.
	FDiagPattern                 = PYQT.Qt.FDiagPattern           # Forward diagonal lines.
	DiagCrossPattern             = PYQT.Qt.DiagCrossPattern       # Crossing diagonal lines.
	LinearGradientPattern        = PYQT.Qt.LinearGradientPattern  # Linear gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	ConicalGradientPattern       = PYQT.Qt.ConicalGradientPattern # Conical gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	RadialGradientPattern        = PYQT.Qt.RadialGradientPattern  # Radial gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	TexturePattern               = PYQT.Qt.TexturePattern         # Custom pattern (see QBrush.setTexture() ).
########################################################################
class DropActions:
	CopyAction                   = PYQT.Qt.CopyAction       # Copy the data to the target.
	MoveAction                   = PYQT.Qt.MoveAction       # Move the data from the source to the target.
	LinkAction                   = PYQT.Qt.LinkAction       # Create a link from the source to the target.
	ActionMask                   = PYQT.Qt.ActionMask       #
	IgnoreAction                 = PYQT.Qt.IgnoreAction     # Ignore the action (do nothing with the data).
	TargetMoveAction             = PYQT.Qt.TargetMoveAction # On Windows, this value is used when the ownership of the D&D data should be taken over by the target application, i.e., the source application should not delete the data. .. raw:: html <br /> On X11 this value is used to do a move. .. raw:: html <br /> TargetMoveAction is not used on the Mac.
########################################################################
class GestureTypes:
	TapGesture                   = PYQT.Qt.TapGesture           # A Tap gesture.
	TapAndHoldGesture            = PYQT.Qt.TapAndHoldGesture    # A Tap-And-Hold (Long-Tap) gesture.
	PanGesture                   = PYQT.Qt.PanGesture           # A Pan gesture.
	PinchGesture                 = PYQT.Qt.PinchGesture         # A Pinch gesture.
	SwipeGesture                 = PYQT.Qt.SwipeGesture         # A Swipe gesture.
	CustomGesture                = PYQT.Qt.CustomGesture        # A flag that can be used to test if the gesture is a user-defined gesture ID.
########################################################################
class CheckStates:
	Unchecked                    = PYQT.Qt.Unchecked           # The item is unchecked.
	PartiallyChecked             = PYQT.Qt.PartiallyChecked    # The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, of their children are checked
	Checked                      = PYQT.Qt.Checked             # The item is checked.
########################################################################
class ItemFlag:
	NoItemFlags                  = PYQT.Qt.NoItemFlags         # It does not have any properties set.
	IsSelectable                 = PYQT.Qt.ItemIsSelectable    # It can be selected.
	IsEditable                   = PYQT.Qt.ItemIsEditable      # It can be edited.
	IsDragEnabled                = PYQT.Qt.ItemIsDragEnabled   # It can be dragged.
	IsDropEnabled                = PYQT.Qt.ItemIsDropEnabled   # It can be used as a drop target.
	IsUserCheckable              = PYQT.Qt.ItemIsUserCheckable # It can be checked or unchecked by the user.
	IsEnabled                    = PYQT.Qt.ItemIsEnabled       # The user can interact with the item.
	IsTristate                   = PYQT.Qt.ItemIsTristate      # The item is checkable with three separate states.
########################################################################
class AlignmentFlag:
	class Horizontal:
		Left    = PYQT.Qt.AlignmentFlag.AlignLeft     # Aligns with the left edge.
		Right   = PYQT.Qt.AlignmentFlag.AlignRight    # Aligns with the right edge.
		Center  = PYQT.Qt.AlignmentFlag.AlignHCenter  # Centers horizontally in the available space.
		Justify = PYQT.Qt.AlignmentFlag.AlignJustify  # Justifies the text in the available space.
		Values  = {'Center' : Center , Center : Center  , Center.name : Center, 
		           'Left'   : Left   , Left   : Left    , Left.name   : Left, 
		           'Justify': Justify, Justify: Justify , Justify.name: Justify, 
		           'Right'  : Right  , Right  : Right   , Right.name  : Right}
	class Vertical:
		Top     = PYQT.Qt.AlignmentFlag.AlignTop     # Aligns with the top.
		Bottom  = PYQT.Qt.AlignmentFlag.AlignBottom  # Aligns with the bottom.
		Center  = PYQT.Qt.AlignmentFlag.AlignVCenter # Centers vertically in the available space.
		Values  = {'Top'    : Top   , Top     : Top   , Top.name     : Top, 
		           'Bottom' : Bottom, Bottom  : Bottom, Bottom.name  : Bottom, 
		           'Center' : Center, Center  : Center, Center.name  : Center}
	class Masks:
		Horizontal = PYQT.Qt.AlignmentFlag.AlignHorizontal_Mask
		Vertical   = PYQT.Qt.AlignmentFlag.AlignVertical_Mask
		Values     = {'Horizontal': Horizontal, Horizontal : "Horizontal",
		              'Vertical'  : Vertical  , Vertical   : "Vertical"}
	Center = PYQT.Qt.AlignmentFlag.AlignCenter # Centers in both dimensions.
########################################################################
class MatchFlag:
	CaseSensitive                = PYQT.Qt.MatchCaseSensitive
	Contains                     = PYQT.Qt.MatchContains
	EndsWith                     = PYQT.Qt.MatchEndsWith
	Exactly                      = PYQT.Qt.MatchExactly
	FixedString                  = PYQT.Qt.MatchFixedString
	Recursive                    = PYQT.Qt.MatchRecursive
	RegExp                       = PYQT.Qt.MatchRegExp
	StartsWith                   = PYQT.Qt.MatchStartsWith
	Wildcard                     = PYQT.Qt.MatchWildcard
	Wrap                         = PYQT.Qt.MatchWrap
########################################################################
class DayOfWeek:
	Friday                       = PYQT.Qt.Friday
	Monday                       = PYQT.Qt.Monday
	Saturday                     = PYQT.Qt.Saturday
	Sunday                       = PYQT.Qt.Sunday
	Thursday                     = PYQT.Qt.Thursday
	Tuesday                      = PYQT.Qt.Tuesday
	Wednesday                    = PYQT.Qt.Wednesday
########################################################################
class MouseButton:
	RightButton                  = PYQT.Qt.RightButton
	MiddleButton                 = PYQT.Qt.MiddleButton
	NoButton                     = PYQT.Qt.NoButton
	LeftButton                   = PYQT.Qt.LeftButton
	MouseButtonMask              = PYQT.Qt.MouseButtonMask
	XButton1                     = PYQT.Qt.XButton1
	XButton2                     = PYQT.Qt.XButton2
	MidButton                    = PYQT.Qt.MidButton
########################################################################
class Modifier:
	CTRL                         = PYQT.Qt.CTRL
	SHIFT                        = PYQT.Qt.SHIFT
	UNICODE_ACCEL                = PYQT.Qt.UNICODE_ACCEL
	MODIFIER_MASK                = PYQT.Qt.MODIFIER_MASK
	META                         = PYQT.Qt.META
	ALT                          = PYQT.Qt.ALT
########################################################################
class SizeHint:
	MinimumDescent               = PYQT.Qt.MinimumDescent
	PreferredSize                = PYQT.Qt.PreferredSize
	MinimumSize                  = PYQT.Qt.MinimumSize
	MaximumSize                  = PYQT.Qt.MaximumSize
########################################################################
class TextFlag:
	TextShowMnemonic             = PYQT.Qt.TextShowMnemonic
	TextHideMnemonic             = PYQT.Qt.TextHideMnemonic
	TextJustificationForced      = PYQT.Qt.TextJustificationForced
	TextDontClip                 = PYQT.Qt.TextDontClip
	TextIncludeTrailingSpaces    = PYQT.Qt.TextIncludeTrailingSpaces
	TextDontPrint                = PYQT.Qt.TextDontPrint
	TextSingleLine               = PYQT.Qt.TextSingleLine
	TextWrapAnywhere             = PYQT.Qt.TextWrapAnywhere
	TextExpandTabs               = PYQT.Qt.TextExpandTabs
	TextWordWrap                 = PYQT.Qt.TextWordWrap
########################################################################
class Colors:
	""""""
	WHITE        = PYQT.Qt.white       #ffffff
	BLACK        = PYQT.Qt.black       #000000
	RED          = PYQT.Qt.red         #ff0000
	DARK_RED     = PYQT.Qt.darkRed     #800000
	GREEN        = PYQT.Qt.green       #00ff00
	DARK_GREEN   = PYQT.Qt.darkGreen	  #008000
	BLUE         = PYQT.Qt.blue        #0000ff
	DARK_BLUE    = PYQT.Qt.darkBlue    #000080
	CYAN         = PYQT.Qt.cyan        #00ffff
	DARK_CYAN    = PYQT.Qt.darkCyan    #008080
	MAGENTA      = PYQT.Qt.magenta     #ff00ff
	DARK_MAGENTA = PYQT.Qt.darkMagenta #800080
	YELLOW       = PYQT.Qt.yellow      #ffff00
	DARK_YELLOW  = PYQT.Qt.darkYellow  #808000
	GRAY         = PYQT.Qt.gray        #a0a0a4
	DARK_GRAY    = PYQT.Qt.darkGray    #808080
	LIGHT_GRAY   = PYQT.Qt.lightGray   #c0c0c0
	TRANSPARENT  = PYQT.Qt.transparent # a transparent black value (i.e., PySide.QtGui.QColor (0, 0, 0, 0))
########################################################################
class QSTYLE:
	########################################################################
	class PrimitiveElement:
		FrameStatusBar                  = PYQT.QStyle.PE_FrameStatusBar #Frame
		PanelButtonCommand              = PYQT.QStyle.PE_PanelButtonCommand #Button used to initiate an action, for example, a PySide.QtGui.QPushButton .
		FrameDefaultButton              = PYQT.QStyle.PE_FrameDefaultButton #This frame around a default button, e.g. in a dialog.
		PanelButtonBevel                = PYQT.QStyle.PE_PanelButtonBevel #Generic panel with a button bevel.
		PanelButtonTool                 = PYQT.QStyle.PE_PanelButtonTool #Panel for a Tool button, used with PySide.QtGui.QToolButton .
		PanelLineEdit                   = PYQT.QStyle.PE_PanelLineEdit #Panel for a PySide.QtGui.QLineEdit .
		IndicatorButtonDropDown         = PYQT.QStyle.PE_IndicatorButtonDropDown #Indicator for a drop down button, for example, a tool button that displays a menu.
		FrameFocusRect                  = PYQT.QStyle.PE_FrameFocusRect #Generic focus indicator.
		IndicatorArrowUp                = PYQT.QStyle.PE_IndicatorArrowUp #Generic Up arrow.
		IndicatorArrowDown              = PYQT.QStyle.PE_IndicatorArrowDown #Generic Down arrow.
		IndicatorArrowRight             = PYQT.QStyle.PE_IndicatorArrowRight #Generic Right arrow.
		IndicatorArrowLeft              = PYQT.QStyle.PE_IndicatorArrowLeft #Generic Left arrow.
		IndicatorSpinUp                 = PYQT.QStyle.PE_IndicatorSpinUp #Up symbol for a spin widget, for example a PySide.QtGui.QSpinBox .
		IndicatorSpinDown               = PYQT.QStyle.PE_IndicatorSpinDown #Down symbol for a spin widget.
		IndicatorSpinPlus               = PYQT.QStyle.PE_IndicatorSpinPlus #Increase symbol for a spin widget.
		IndicatorSpinMinus              = PYQT.QStyle.PE_IndicatorSpinMinus #Decrease symbol for a spin widget.
		IndicatorItemViewItemCheck      = PYQT.QStyle.PE_IndicatorItemViewItemCheck #On/off indicator for a view item.
		IndicatorCheckBox               = PYQT.QStyle.PE_IndicatorCheckBox #On/off indicator, for example, a PySide.QtGui.QCheckBox .
		IndicatorRadioButton            = PYQT.QStyle.PE_IndicatorRadioButton #Exclusive on/off indicator, for example, a PySide.QtGui.QRadioButton .
		IndicatorDockWidgetResizeHandle = PYQT.QStyle.PE_IndicatorDockWidgetResizeHandle #Resize handle for dock windows.
		Frame                           = PYQT.QStyle.PE_Frame #Generic frame
		FrameMenu                       = PYQT.QStyle.PE_FrameMenu #Frame for popup windows/menus; see also PySide.QtGui.QMenu .
		PanelMenuBar                    = PYQT.QStyle.PE_PanelMenuBar #Panel for menu bars.
		PanelScrollAreaCorner           = PYQT.QStyle.PE_PanelScrollAreaCorner #Panel at the bottom-right (or bottom-left) corner of a scroll area.
		FrameDockWidget                 = PYQT.QStyle.PE_FrameDockWidget #Panel frame for dock windows and toolbars.
		FrameTabWidget                  = PYQT.QStyle.PE_FrameTabWidget #Frame for tab widgets.
		FrameLineEdit                   = PYQT.QStyle.PE_FrameLineEdit #Panel frame for line edits.
		FrameGroupBox                   = PYQT.QStyle.PE_FrameGroupBox #Panel frame around group boxes.
		FrameButtonBevel                = PYQT.QStyle.PE_FrameButtonBevel #Panel frame for a button bevel.
		FrameButtonTool                 = PYQT.QStyle.PE_FrameButtonTool #Panel frame for a tool button.
		IndicatorHeaderArrow            = PYQT.QStyle.PE_IndicatorHeaderArrow #Arrow used to indicate sorting on a list or table header.
		FrameStatusBarItem              = PYQT.QStyle.PE_FrameStatusBarItem #Frame for an item of a status bar; see also PySide.QtGui.QStatusBar .
		FrameWindow                     = PYQT.QStyle.PE_FrameWindow #Frame around a MDI window or a docking window.
		IndicatorMenuCheckMark          = PYQT.QStyle.PE_IndicatorMenuCheckMark #Check mark used in a menu.
		IndicatorProgressChunk          = PYQT.QStyle.PE_IndicatorProgressChunk #Section of a progress bar indicator; see also PySide.QtGui.QProgressBar .
		IndicatorBranch                 = PYQT.QStyle.PE_IndicatorBranch #Lines used to represent the branch of a tree in a tree view.
		IndicatorToolBarHandle          = PYQT.QStyle.PE_IndicatorToolBarHandle #The handle of a toolbar.
		IndicatorToolBarSeparator       = PYQT.QStyle.PE_IndicatorToolBarSeparator #The separator in a toolbar.
		PanelToolBar                    = PYQT.QStyle.PE_PanelToolBar #The panel for a toolbar.
		PanelTipLabel                   = PYQT.QStyle.PE_PanelTipLabel #The panel for a tip label.
		FrameTabBarBase                 = PYQT.QStyle.PE_FrameTabBarBase
		IndicatorTabTear                = PYQT.QStyle.PE_IndicatorTabTear #An indicator that a tab is partially scrolled out of the visible tab bar when there are many tabs.
		IndicatorColumnViewArrow        = PYQT.QStyle.PE_IndicatorColumnViewArrow #An arrow in a PySide.QtGui.QColumnView .
		Widget                          = PYQT.QStyle.PE_Widget #A plain PySide.QtGui.QWidget .
		CustomBase                      = PYQT.QStyle.PE_CustomBase #Base value for custom primitive elements. All values above this are reserved for custom use. Custom values must be greater than this value.
		IndicatorItemViewItemDrop       = PYQT.QStyle.PE_IndicatorItemViewItemDrop #An indicator that is drawn to show where an item in an item view is about to be dropped during a drag-and-drop operation in an item view.
		PanelItemViewItem               = PYQT.QStyle.PE_PanelItemViewItem #The background for an item in an item view.
		PanelItemViewRow                = PYQT.QStyle.PE_PanelItemViewRow #The background of a row in an item view.
		PanelStatusBar                  = PYQT.QStyle.PE_PanelStatusBar #The panel for a status bar.
		IndicatorTabClose               = PYQT.QStyle.PE_IndicatorTabClose #The close button on a tab bar.
		PanelMenu                       = PYQT.QStyle.PE_PanelMenu #The panel for a menu.
	########################################################################
	class StyleHint:
		EtchDisabledText                               = PYQT.QStyle.SH_EtchDisabledText #Disabled text is etched as it is on Windows.
		DitherDisabledText                             = PYQT.QStyle.SH_DitherDisabledText #Disabled text is dithered as it is on Motif.
		ScrollBar_ContextMenu                          = PYQT.QStyle.SH_ScrollBar_ContextMenu #Whether or not a scroll bar has a context menu.
		ScrollBar_MiddleClickAbsolutePosition          = PYQT.QStyle.SH_ScrollBar_MiddleClickAbsolutePosition #A boolean value. If true, middle clicking on a scroll bar causes the slider to jump to that position. If false, middle clicking is ignored.
		ScrollBar_LeftClickAbsolutePosition            = PYQT.QStyle.SH_ScrollBar_LeftClickAbsolutePosition #A boolean value. If true, left clicking on a scroll bar causes the slider to jump to that position. If false, left clicking will behave as appropriate for each control.
		ScrollBar_ScrollWhenPointerLeavesControl       = PYQT.QStyle.SH_ScrollBar_ScrollWhenPointerLeavesControl #A boolean value. If true, when clicking a scroll bar QStyle.SubControl , holding the mouse button down and moving the pointer outside the QStyle.SubControl , the scroll bar continues to scroll. If false, the scollbar stops scrolling when the pointer leaves the QStyle.SubControl .
		ScrollBar_RollBetweenButtons                   = PYQT.QStyle.SH_ScrollBar_RollBetweenButtons #A boolean value. If true, when clicking a scroll bar button ( SC_ScrollBarAddLine or SC_ScrollBarSubLine ) and dragging over to the opposite button (rolling) will press the new button and release the old one. When it is false, the original button is released and nothing happens (like a push button).
		TabBar_Alignment                               = PYQT.QStyle.SH_TabBar_Alignment #The alignment for tabs in a PySide.QtGui.QTabWidget . Possible values are Qt.AlignLeft , Qt.AlignCenter and Qt.AlignRight .
		Header_ArrowAlignment                          = PYQT.QStyle.SH_Header_ArrowAlignment #The placement of the sorting indicator may appear in list or table headers. Possible values are Qt.Left or Qt.Right .
		Slider_SnapToValue                             = PYQT.QStyle.SH_Slider_SnapToValue #Sliders snap to values while moving, as they do on Windows.
		Slider_SloppyKeyEvents                         = PYQT.QStyle.SH_Slider_SloppyKeyEvents #Key presses handled in a sloppy manner, i.e., left on a vertical slider subtracts a line.
		ProgressDialog_CenterCancelButton              = PYQT.QStyle.SH_ProgressDialog_CenterCancelButton #Center button on progress dialogs, like Motif, otherwise right aligned.
		ProgressDialog_TextLabelAlignment              = PYQT.QStyle.SH_ProgressDialog_TextLabelAlignment #The alignment for text labels in progress dialogs; Qt.AlignCenter on Windows, Qt.AlignVCenter otherwise.
		PrintDialog_RightAlignButtons                  = PYQT.QStyle.SH_PrintDialog_RightAlignButtons #Right align buttons in the print dialog, as done on Windows.
		MainWindow_SpaceBelowMenuBar                   = PYQT.QStyle.SH_MainWindow_SpaceBelowMenuBar #One or two pixel space between the menu bar and the dockarea, as done on Windows.
		FontDialog_SelectAssociatedText                = PYQT.QStyle.SH_FontDialog_SelectAssociatedText #Select the text in the line edit, or when selecting an item from the listbox, or when the line edit receives focus, as done on Windows.
		Menu_KeyboardSearch                            = PYQT.QStyle.SH_Menu_KeyboardSearch #Typing causes a menu to be search for relevant items, otherwise only mnemnonic is considered.
		Menu_AllowActiveAndDisabled                    = PYQT.QStyle.SH_Menu_AllowActiveAndDisabled #Allows disabled menu items to be active.
		Menu_SpaceActivatesItem                        = PYQT.QStyle.SH_Menu_SpaceActivatesItem #Pressing the space bar activates the item, as done on Motif.
		Menu_SubMenuPopupDelay                         = PYQT.QStyle.SH_Menu_SubMenuPopupDelay #The number of milliseconds to wait before opening a submenu (256 on Windows, 96 on Motif).
		Menu_Scrollable                                = PYQT.QStyle.SH_Menu_Scrollable #Whether popup menus must support scrolling.
		Menu_SloppySubMenus                            = PYQT.QStyle.SH_Menu_SloppySubMenus #Whether popupmenus must support sloppy submenu; as implemented on Mac OS.
		ScrollView_FrameOnlyAroundContents             = PYQT.QStyle.SH_ScrollView_FrameOnlyAroundContents #Whether scrollviews draw their frame only around contents (like Motif), or around contents, scroll bars and corner widgets (like Windows).
		MenuBar_AltKeyNavigation                       = PYQT.QStyle.SH_MenuBar_AltKeyNavigation #Menu bars items are navigable by pressing Alt, followed by using the arrow keys to select the desired item.
		ComboBox_ListMouseTracking                     = PYQT.QStyle.SH_ComboBox_ListMouseTracking #Mouse tracking in combobox drop-down lists.
		Menu_MouseTracking                             = PYQT.QStyle.SH_Menu_MouseTracking #Mouse tracking in popup menus.
		MenuBar_MouseTracking                          = PYQT.QStyle.SH_MenuBar_MouseTracking #Mouse tracking in menu bars.
		Menu_FillScreenWithScroll                      = PYQT.QStyle.SH_Menu_FillScreenWithScroll #Whether scrolling popups should fill the screen as they are scrolled.
		Menu_SelectionWrap                             = PYQT.QStyle.SH_Menu_SelectionWrap #Whether popups should allow the selections to wrap, that is when selection should the next item be the first item.
		ItemView_ChangeHighlightOnFocus                = PYQT.QStyle.SH_ItemView_ChangeHighlightOnFocus #Gray out selected items when losing focus.
		Widget_ShareActivation                         = PYQT.QStyle.SH_Widget_ShareActivation #Turn on sharing activation with floating modeless dialogs.
		TabBar_SelectMouseType                         = PYQT.QStyle.SH_TabBar_SelectMouseType #Which type of mouse event should cause a tab to be selected.
		TabBar_PreferNoArrows                          = PYQT.QStyle.SH_TabBar_PreferNoArrows #Whether a tab bar should suggest a size to prevent scoll arrows.
		ComboBox_Popup                                 = PYQT.QStyle.SH_ComboBox_Popup #Allows popups as a combobox drop-down menu.
		Workspace_FillSpaceOnMaximize                  = PYQT.QStyle.SH_Workspace_FillSpaceOnMaximize #The workspace should maximize the client area.
		TitleBar_NoBorder                              = PYQT.QStyle.SH_TitleBar_NoBorder #The title bar has no border.
		ScrollBar_StopMouseOverSlider                  = PYQT.QStyle.SH_ScrollBar_StopMouseOverSlider #Obsolete. Use SH_Slider_StopMouseOverSlider instead.
		Slider_StopMouseOverSlider                     = PYQT.QStyle.SH_Slider_StopMouseOverSlider #Stops auto-repeat when the slider reaches the mouse position.
		BlinkCursorWhenTextSelected                    = PYQT.QStyle.SH_BlinkCursorWhenTextSelected #Whether cursor should blink when text is selected.
		RichText_FullWidthSelection                    = PYQT.QStyle.SH_RichText_FullWidthSelection #Whether richtext selections should extend to the full width of the document.
		GroupBox_TextLabelVerticalAlignment            = PYQT.QStyle.SH_GroupBox_TextLabelVerticalAlignment #How to vertically align a group boxs text label.
		GroupBox_TextLabelColor                        = PYQT.QStyle.SH_GroupBox_TextLabelColor #How to paint a group boxs text label.
		DialogButtons_DefaultButton                    = PYQT.QStyle.SH_DialogButtons_DefaultButton #Which button gets the default status in a dialogs button widget.
		ToolBox_SelectedPageTitleBold                  = PYQT.QStyle.SH_ToolBox_SelectedPageTitleBold #Boldness of the selected page title in a PySide.QtGui.QToolBox .
		LineEdit_PasswordCharacter                     = PYQT.QStyle.SH_LineEdit_PasswordCharacter #The Unicode character to be used for passwords.
		Table_GridLineColor                            = PYQT.QStyle.SH_Table_GridLineColor #The RGB value of the grid for a table.
		UnderlineShortcut                              = PYQT.QStyle.SH_UnderlineShortcut #Whether shortcuts are underlined.
		SpellCheckUnderlineStyle                       = PYQT.QStyle.SH_SpellCheckUnderlineStyle #A QTextCharFormat.UnderlineStyle value that specifies the way misspelled words should be underlined.
		SpinBox_AnimateButton                          = PYQT.QStyle.SH_SpinBox_AnimateButton #Animate a click when up or down is pressed in a spin box.
		SpinBox_KeyPressAutoRepeatRate                 = PYQT.QStyle.SH_SpinBox_KeyPressAutoRepeatRate #Auto-repeat interval for spinbox key presses.
		SpinBox_ClickAutoRepeatRate                    = PYQT.QStyle.SH_SpinBox_ClickAutoRepeatRate #Auto-repeat interval for spinbox mouse clicks.
		SpinBox_ClickAutoRepeatThreshold               = PYQT.QStyle.SH_SpinBox_ClickAutoRepeatThreshold #Auto-repeat threshold for spinbox mouse clicks.
		ToolTipLabel_Opacity                           = PYQT.QStyle.SH_ToolTipLabel_Opacity #An integer indicating the opacity for the tip label, 0 is completely transparent, 255 is completely opaque.
		DrawMenuBarSeparator                           = PYQT.QStyle.SH_DrawMenuBarSeparator #Indicates whether or not the menu bar draws separators.
		TitleBar_ModifyNotification                    = PYQT.QStyle.SH_TitleBar_ModifyNotification #Indicates if the title bar should show a * for windows that are modified.
		Button_FocusPolicy                             = PYQT.QStyle.SH_Button_FocusPolicy #The default focus policy for buttons.
		CustomBase                                     = PYQT.QStyle.SH_CustomBase #Base value for custom style hints. Custom values must be greater than this value.
		MessageBox_UseBorderForButtonSpacing           = PYQT.QStyle.SH_MessageBox_UseBorderForButtonSpacing #A boolean indicating what the to use the border of the buttons (computed as half the button height) for the spacing of the button in a message box.
		MessageBox_CenterButtons                       = PYQT.QStyle.SH_MessageBox_CenterButtons #A boolean indicating whether the buttons in the message box should be centered or not (see QDialogButtonBox::setCentered()).
		MessageBox_TextInteractionFlags                = PYQT.QStyle.SH_MessageBox_TextInteractionFlags #A boolean indicating if the text in a message box should allow user interfactions (e.g. selection) or not.
		TitleBar_AutoRaise                             = PYQT.QStyle.SH_TitleBar_AutoRaise #A boolean indicating whether controls on a title bar ought to update when the mouse is over them.
		ToolButton_PopupDelay                          = PYQT.QStyle.SH_ToolButton_PopupDelay #An int indicating the popup delay in milliseconds for menus attached to tool buttons.
		FocusFrame_Mask                                = PYQT.QStyle.SH_FocusFrame_Mask #The mask of the focus frame.
		RubberBand_Mask                                = PYQT.QStyle.SH_RubberBand_Mask #The mask of the rubber band.
		WindowFrame_Mask                               = PYQT.QStyle.SH_WindowFrame_Mask #The mask of the window frame.
		SpinControls_DisableOnBounds                   = PYQT.QStyle.SH_SpinControls_DisableOnBounds #Determines if the spin controls will shown as disabled when reaching the spin range boundary.
		Dial_BackgroundRole                            = PYQT.QStyle.SH_Dial_BackgroundRole #Defines the styles preferred background role (as QPalette.ColorRole ) for a dial widget.
		ComboBox_LayoutDirection                       = PYQT.QStyle.SH_ComboBox_LayoutDirection #The layout direction for the combo box. By default it should be the same as indicated by the QStyleOption.direction variable.
		ItemView_EllipsisLocation                      = PYQT.QStyle.SH_ItemView_EllipsisLocation #The location where ellipses should be added for item text that is too long to fit in an view item.
		ItemView_ShowDecorationSelected                = PYQT.QStyle.SH_ItemView_ShowDecorationSelected #When an item in an item view is selected, also highlight the branch or other decoration.
		ItemView_ActivateItemOnSingleClick             = PYQT.QStyle.SH_ItemView_ActivateItemOnSingleClick #Emit the activated signal when the user single clicks on an item in an item in an item view. Otherwise the signal is emitted when the user double clicks on an item.
		Slider_AbsoluteSetButtons                      = PYQT.QStyle.SH_Slider_AbsoluteSetButtons #Which mouse buttons cause a slider to set the value to the position clicked on.
		Slider_PageSetButtons                          = PYQT.QStyle.SH_Slider_PageSetButtons #Which mouse buttons cause a slider to page step the value.
		TabBar_ElideMode                               = PYQT.QStyle.SH_TabBar_ElideMode #The default eliding style for a tab bar.
		DialogButtonLayout                             = PYQT.QStyle.SH_DialogButtonLayout #Controls how buttons are laid out in a PySide.QtGui.QDialogButtonBox , returns a QDialogButtonBox.ButtonLayout enum.
		WizardStyle                                    = PYQT.QStyle.SH_WizardStyle #Controls the look and feel of a PySide.QtGui.QWizard . Returns a QWizard.WizardStyle enum.
		FormLayoutWrapPolicy                           = PYQT.QStyle.SH_FormLayoutWrapPolicy #Provides a default for how rows are wrapped in a PySide.QtGui.QFormLayout . Returns a QFormLayout.RowWrapPolicy enum.
		FormLayoutFieldGrowthPolicy                    = PYQT.QStyle.SH_FormLayoutFieldGrowthPolicy #Provides a default for how fields can grow in a PySide.QtGui.QFormLayout . Returns a QFormLayout.FieldGrowthPolicy enum.
		FormLayoutFormAlignment                        = PYQT.QStyle.SH_FormLayoutFormAlignment #Provides a default for how a PySide.QtGui.QFormLayout aligns its contents within the available space. Returns a Qt.Alignment enum.
		FormLayoutLabelAlignment                       = PYQT.QStyle.SH_FormLayoutLabelAlignment #Provides a default for how a PySide.QtGui.QFormLayout aligns labels within the available space. Returns a Qt.Alignment enum.
		ItemView_ArrowKeysNavigateIntoChildren         = PYQT.QStyle.SH_ItemView_ArrowKeysNavigateIntoChildren #Controls whether the tree view will select the first child when it is exapanded and the right arrow key is pressed.
		ComboBox_PopupFrameStyle                       = PYQT.QStyle.SH_ComboBox_PopupFrameStyle #The frame style used when drawing a combobox popup menu.
		DialogButtonBox_ButtonsHaveIcons               = PYQT.QStyle.SH_DialogButtonBox_ButtonsHaveIcons #Indicates whether or not StandardButtons in PySide.QtGui.QDialogButtonBox should have icons or not.
		ItemView_MovementWithoutUpdatingSelection      = PYQT.QStyle.SH_ItemView_MovementWithoutUpdatingSelection #The item view is able to indicate a current item without changing the selection.
		ToolTip_Mask                                   = PYQT.QStyle.SH_ToolTip_Mask #The mask of a tool tip.
		FocusFrame_AboveWidget                         = PYQT.QStyle.SH_FocusFrame_AboveWidget #The FocusFrame is stacked above the widget that it is focusing on.
		TextControl_FocusIndicatorTextCharFormat       = PYQT.QStyle.SH_TextControl_FocusIndicatorTextCharFormat #Specifies the text format used to highlight focused anchors in rich text documents displayed for example in PySide.QtGui.QTextBrowser . The format has to be a PySide.QtGui.QTextCharFormat returned in the variant of the PySide.QtGui.QStyleHintReturnVariant return value. The QTextFormat.OutlinePen property is used for the outline and QTextFormat.BackgroundBrush for the background of the highlighted area.
		Menu_FlashTriggeredItem                        = PYQT.QStyle.SH_Menu_FlashTriggeredItem #Flash triggered item.
		Menu_FadeOutOnHide                             = PYQT.QStyle.SH_Menu_FadeOutOnHide #Fade out the menu instead of hiding it immediately.
		TabWidget_DefaultTabPosition                   = PYQT.QStyle.SH_TabWidget_DefaultTabPosition #Default position of the tab bar in a tab widget.
		ToolBar_Movable                                = PYQT.QStyle.SH_ToolBar_Movable #Determines if the tool bar is movable by default.
		ItemView_PaintAlternatingRowColorsForEmptyArea = PYQT.QStyle.SH_ItemView_PaintAlternatingRowColorsForEmptyArea #Whether PySide.QtGui.QTreeView paints alternating row colors for the area that does not have any items.
		Menu_Mask                                      = PYQT.QStyle.SH_Menu_Mask #The mask for a popup menu.
		ItemView_DrawDelegateFrame                     = PYQT.QStyle.SH_ItemView_DrawDelegateFrame #Determines if there should be a frame for a delegate widget.
		TabBar_CloseButtonPosition                     = PYQT.QStyle.SH_TabBar_CloseButtonPosition #Determines the position of the close button on a tab in a tab bar.
		DockWidget_ButtonsHaveFrame                    = PYQT.QStyle.SH_DockWidget_ButtonsHaveFrame #Determines if dockwidget buttons should have frames. Default is true.
		ToolButtonStyle                                = PYQT.QStyle.SH_ToolButtonStyle #Determines the default system style for tool buttons that uses Qt.ToolButtonFollowStyle .
		RequestSoftwareInputPanel                      = PYQT.QStyle.SH_RequestSoftwareInputPanel #Determines when a software input panel should be requested by input widgets. Returns an enum of type QStyle.RequestSoftwareInputPanel .
	########################################################################
	class PixelMetric:
		ButtonMargin                   = PYQT.QStyle.PM_ButtonMargin #Amount of whitespace between push button labels and the frame.
		DockWidgetTitleBarButtonMargin = PYQT.QStyle.PM_DockWidgetTitleBarButtonMargin #Amount of whitespace between dock widgets title bar button labels and the frame.
		ButtonDefaultIndicator         = PYQT.QStyle.PM_ButtonDefaultIndicator #Width of the default-button indicator frame.
		MenuButtonIndicator            = PYQT.QStyle.PM_MenuButtonIndicator #Width of the menu button indicator proportional to the widget height.
		ButtonShiftHorizontal          = PYQT.QStyle.PM_ButtonShiftHorizontal #Horizontal contents shift of a button when the button is down.
		ButtonShiftVertical            = PYQT.QStyle.PM_ButtonShiftVertical #Vertical contents shift of a button when the button is down.
		DefaultFrameWidth              = PYQT.QStyle.PM_DefaultFrameWidth #Default frame width (usually 2).
		SpinBoxFrameWidth              = PYQT.QStyle.PM_SpinBoxFrameWidth #Frame width of a spin box, defaults to PM_DefaultFrameWidth .
		ComboBoxFrameWidth             = PYQT.QStyle.PM_ComboBoxFrameWidth #Frame width of a combo box, defaults to PM_DefaultFrameWidth .
		MDIFrameWidth                  = PYQT.QStyle.PM_MDIFrameWidth #Obsolete. Use PM_MdiSubWindowFrameWidth instead.
		MdiSubWindowFrameWidth         = PYQT.QStyle.PM_MdiSubWindowFrameWidth #Frame width of an MDI window.
		MDIMinimizedWidth              = PYQT.QStyle.PM_MDIMinimizedWidth #Obsolete. Use PM_MdiSubWindowMinimizedWidth instead.
		MdiSubWindowMinimizedWidth     = PYQT.QStyle.PM_MdiSubWindowMinimizedWidth #Width of a minimized MDI window.
		LayoutLeftMargin               = PYQT.QStyle.PM_LayoutLeftMargin #Default left margin for a PySide.QtGui.QLayout .
		LayoutTopMargin                = PYQT.QStyle.PM_LayoutTopMargin #Default top margin for a PySide.QtGui.QLayout .
		LayoutRightMargin              = PYQT.QStyle.PM_LayoutRightMargin #Default right margin for a PySide.QtGui.QLayout .
		LayoutBottomMargin             = PYQT.QStyle.PM_LayoutBottomMargin #Default bottom margin for a PySide.QtGui.QLayout .
		LayoutHorizontalSpacing        = PYQT.QStyle.PM_LayoutHorizontalSpacing #Default horizontal spacing for a PySide.QtGui.QLayout .
		LayoutVerticalSpacing          = PYQT.QStyle.PM_LayoutVerticalSpacing #Default vertical spacing for a PySide.QtGui.QLayout .
		MaximumDragDistance            = PYQT.QStyle.PM_MaximumDragDistance #The maximum allowed distance between the mouse and a scrollbar when dragging. Exceeding the specified distance will cause the slider to jump back to the original position; a value of -1 disables this behavior.
		ScrollBarExtent                = PYQT.QStyle.PM_ScrollBarExtent #Width of a vertical scroll bar and the height of a horizontal scroll bar.
		ScrollBarSliderMin             = PYQT.QStyle.PM_ScrollBarSliderMin #The minimum height of a vertical scroll bars slider and the minimum width of a horizontal scroll bars slider.
		SliderThickness                = PYQT.QStyle.PM_SliderThickness #Total slider thickness.
		SliderControlThickness         = PYQT.QStyle.PM_SliderControlThickness #Thickness of the slider handle.
		SliderLength                   = PYQT.QStyle.PM_SliderLength #Length of the slider.
		SliderTickmarkOffset           = PYQT.QStyle.PM_SliderTickmarkOffset #The offset between the tickmarks and the slider.
		SliderSpaceAvailable           = PYQT.QStyle.PM_SliderSpaceAvailable #The available space for the slider to move.
		DockWidgetSeparatorExtent      = PYQT.QStyle.PM_DockWidgetSeparatorExtent #Width of a separator in a horizontal dock window and the height of a separator in a vertical dock window.
		DockWidgetHandleExtent         = PYQT.QStyle.PM_DockWidgetHandleExtent #Width of the handle in a horizontal dock window and the height of the handle in a vertical dock window.
		DockWidgetFrameWidth           = PYQT.QStyle.PM_DockWidgetFrameWidth #Frame width of a dock window.
		DockWidgetTitleMargin          = PYQT.QStyle.PM_DockWidgetTitleMargin #Margin of the dock window title.
		MenuBarPanelWidth              = PYQT.QStyle.PM_MenuBarPanelWidth #Frame width of a menu bar, defaults to PM_DefaultFrameWidth .
		MenuBarItemSpacing             = PYQT.QStyle.PM_MenuBarItemSpacing #Spacing between menu bar items.
		MenuBarHMargin                 = PYQT.QStyle.PM_MenuBarHMargin #Spacing between menu bar items and left/right of bar.
		MenuBarVMargin                 = PYQT.QStyle.PM_MenuBarVMargin #Spacing between menu bar items and top/bottom of bar.
		ToolBarFrameWidth              = PYQT.QStyle.PM_ToolBarFrameWidth #Width of the frame around toolbars.
		ToolBarHandleExtent            = PYQT.QStyle.PM_ToolBarHandleExtent #Width of a toolbar handle in a horizontal toolbar and the height of the handle in a vertical toolbar.
		ToolBarItemMargin              = PYQT.QStyle.PM_ToolBarItemMargin #Spacing between the toolbar frame and the items.
		ToolBarItemSpacing             = PYQT.QStyle.PM_ToolBarItemSpacing #Spacing between toolbar items.
		ToolBarSeparatorExtent         = PYQT.QStyle.PM_ToolBarSeparatorExtent #Width of a toolbar separator in a horizontal toolbar and the height of a separator in a vertical toolbar.
		ToolBarExtensionExtent         = PYQT.QStyle.PM_ToolBarExtensionExtent #Width of a toolbar extension button in a horizontal toolbar and the height of the button in a vertical toolbar.
		TabBarTabOverlap               = PYQT.QStyle.PM_TabBarTabOverlap #Number of pixels the tabs should overlap. (Currently only used in styles, not inside of PySide.QtGui.QTabBar )
		TabBarTabHSpace                = PYQT.QStyle.PM_TabBarTabHSpace #Extra space added to the tab width.
		TabBarTabVSpace                = PYQT.QStyle.PM_TabBarTabVSpace #Extra space added to the tab height.
		TabBarBaseHeight               = PYQT.QStyle.PM_TabBarBaseHeight #Height of the area between the tab bar and the tab pages.
		TabBarBaseOverlap              = PYQT.QStyle.PM_TabBarBaseOverlap #Number of pixels the tab bar overlaps the tab bar base.
		TabBarScrollButtonWidt         = PYQT.QStyle.PM_TabBarScrollButtonWidth #
		TabBarTabShiftHorizontal       = PYQT.QStyle.PM_TabBarTabShiftHorizontal #Horizontal pixel shift when a tab is selected.
		TabBarTabShiftVertical         = PYQT.QStyle.PM_TabBarTabShiftVertical #Vertical pixel shift when a tab is selected.
		ProgressBarChunkWidth          = PYQT.QStyle.PM_ProgressBarChunkWidth #Width of a chunk in a progress bar indicator.
		SplitterWidth                  = PYQT.QStyle.PM_SplitterWidth #Width of a splitter.
		TitleBarHeight                 = PYQT.QStyle.PM_TitleBarHeight #Height of the title bar.
		IndicatorWidth                 = PYQT.QStyle.PM_IndicatorWidth #Width of a check box indicator.
		IndicatorHeight                = PYQT.QStyle.PM_IndicatorHeight #Height of a checkbox indicator.
		ExclusiveIndicatorWidth        = PYQT.QStyle.PM_ExclusiveIndicatorWidth #Width of a radio button indicator.
		ExclusiveIndicatorHeight       = PYQT.QStyle.PM_ExclusiveIndicatorHeight #Height of a radio button indicator.
		MenuPanelWidth                 = PYQT.QStyle.PM_MenuPanelWidth #Border width (applied on all sides) for a PySide.QtGui.QMenu .
		MenuHMargin                    = PYQT.QStyle.PM_MenuHMargin #Additional border (used on left and right) for a PySide.QtGui.QMenu .
		MenuVMargin                    = PYQT.QStyle.PM_MenuVMargin #Additional border (used for bottom and top) for a PySide.QtGui.QMenu .
		MenuScrollerHeight             = PYQT.QStyle.PM_MenuScrollerHeight #Height of the scroller area in a PySide.QtGui.QMenu .
		MenuTearoffHeight              = PYQT.QStyle.PM_MenuTearoffHeight #Height of a tear off area in a PySide.QtGui.QMenu .
		MenuDesktopFrameWidth          = PYQT.QStyle.PM_MenuDesktopFrameWidth #The frame width for the menu on the desktop.
		HeaderMarkSize                 = PYQT.QStyle.PM_HeaderMarkSize #The size of the sort indicator in a header.
		HeaderGripMargin               = PYQT.QStyle.PM_HeaderGripMargin #The size of the resize grip in a header.
		HeaderMargin                   = PYQT.QStyle.PM_HeaderMargin #The size of the margin between the sort indicator and the text.
		SpinBoxSliderHeight            = PYQT.QStyle.PM_SpinBoxSliderHeight #The height of the optional spin box slider.
		ToolBarIconSize                = PYQT.QStyle.PM_ToolBarIconSize #Default tool bar icon size
		SmallIconSize                  = PYQT.QStyle.PM_SmallIconSize #Default small icon size
		LargeIconSize                  = PYQT.QStyle.PM_LargeIconSize #Default large icon size
		FocusFrameHMargin              = PYQT.QStyle.PM_FocusFrameHMargin #Horizontal margin that the focus frame will outset the widget by.
		FocusFrameVMargin              = PYQT.QStyle.PM_FocusFrameVMargin #Vertical margin that the focus frame will outset the widget by.
		IconViewIconSize               = PYQT.QStyle.PM_IconViewIconSize #The default size for icons in an icon view.
		ListViewIconSize               = PYQT.QStyle.PM_ListViewIconSize #The default size for icons in a list view.
		ToolTipLabelFrameWidth         = PYQT.QStyle.PM_ToolTipLabelFrameWidth #The frame width for a tool tip label.
		CheckBoxLabelSpacing           = PYQT.QStyle.PM_CheckBoxLabelSpacing #The spacing between a check box indicator and its label.
		RadioButtonLabelSpacing        = PYQT.QStyle.PM_RadioButtonLabelSpacing #The spacing between a radio button indicator and its label.
		TabBarIconSize                 = PYQT.QStyle.PM_TabBarIconSize #The default icon size for a tab bar.
		SizeGripSize                   = PYQT.QStyle.PM_SizeGripSize #The size of a size grip.
		MessageBoxIconSize             = PYQT.QStyle.PM_MessageBoxIconSize #The size of the standard icons in a message box
		ButtonIconSize                 = PYQT.QStyle.PM_ButtonIconSize #The default size of button icons
		TextCursorWidth                = PYQT.QStyle.PM_TextCursorWidth #The width of the cursor in a line edit or text edit
		TabBar_ScrollButtonOverlap     = PYQT.QStyle.PM_TabBar_ScrollButtonOverlap #The distance between the left and right buttons in a tab bar.
		TabCloseIndicatorWidth         = PYQT.QStyle.PM_TabCloseIndicatorWidth #The default width of a close button on a tab in a tab bar.
		TabCloseIndicatorHeight        = PYQT.QStyle.PM_TabCloseIndicatorHeight #The default height of a close button on a tab in a tab bar.
		CustomBase                     = PYQT.QStyle.PM_CustomBase #Base value for custom pixel metrics. Custom values must be greater than this value.
	########################################################################
	class StandardPixmap:
		TitleBarMinButton                = PYQT.QStyle.SP_TitleBarMinButton #Minimize button on title bars (e.g., in PySide.QtGui.QMdiSubWindow ).
		TitleBarMenuButton               = PYQT.QStyle.SP_TitleBarMenuButton #Menu button on a title bar.
		TitleBarMaxButton                = PYQT.QStyle.SP_TitleBarMaxButton #Maximize button on title bars.
		TitleBarCloseButton              = PYQT.QStyle.SP_TitleBarCloseButton #Close button on title bars.
		TitleBarNormalButton             = PYQT.QStyle.SP_TitleBarNormalButton #Normal (restore) button on title bars.
		TitleBarShadeButton              = PYQT.QStyle.SP_TitleBarShadeButton #Shade button on title bars.
		TitleBarUnshadeButton            = PYQT.QStyle.SP_TitleBarUnshadeButton #Unshade button on title bars.
		TitleBarContextHelpButton        = PYQT.QStyle.SP_TitleBarContextHelpButton #The Context help button on title bars.
		MessageBoxInformation            = PYQT.QStyle.SP_MessageBoxInformation #The information icon.
		MessageBoxWarning                = PYQT.QStyle.SP_MessageBoxWarning #The warning icon.
		MessageBoxCritical               = PYQT.QStyle.SP_MessageBoxCritical #The critical icon.
		MessageBoxQuestion               = PYQT.QStyle.SP_MessageBoxQuestion #The question icon.
		DesktopIcon                      = PYQT.QStyle.SP_DesktopIcon #The desktop icon.
		TrashIcon                        = PYQT.QStyle.SP_TrashIcon #The trash icon.
		ComputerIcon                     = PYQT.QStyle.SP_ComputerIcon #The My computer icon.
		DriveFDIcon                      = PYQT.QStyle.SP_DriveFDIcon #The floppy icon.
		DriveHDIcon                      = PYQT.QStyle.SP_DriveHDIcon #The harddrive icon.
		DriveCDIcon                      = PYQT.QStyle.SP_DriveCDIcon #The CD icon.
		DriveDVDIcon                     = PYQT.QStyle.SP_DriveDVDIcon #The DVD icon.
		DriveNetIcon                     = PYQT.QStyle.SP_DriveNetIcon #The network icon.
		DirHomeIcon                      = PYQT.QStyle.SP_DirHomeIcon #The home directory icon.
		DirOpenIcon                      = PYQT.QStyle.SP_DirOpenIcon #The open directory icon.
		DirClosedIcon                    = PYQT.QStyle.SP_DirClosedIcon #The closed directory icon.
		DirIcon                          = PYQT.QStyle.SP_DirIcon #The directory icon.
		DirLinkIcon                      = PYQT.QStyle.SP_DirLinkIcon #The link to directory icon.
		FileIcon                         = PYQT.QStyle.SP_FileIcon #The file icon.
		FileLinkIcon                     = PYQT.QStyle.SP_FileLinkIcon #The link to file icon.
		FileDialogStart                  = PYQT.QStyle.SP_FileDialogStart #The start icon in a file dialog.
		FileDialogEnd                    = PYQT.QStyle.SP_FileDialogEnd #The end icon in a file dialog.
		FileDialogToParent               = PYQT.QStyle.SP_FileDialogToParent #The parent directory icon in a file dialog.
		FileDialogNewFolder              = PYQT.QStyle.SP_FileDialogNewFolder #The create new folder icon in a file dialog.
		FileDialogDetailedView           = PYQT.QStyle.SP_FileDialogDetailedView #The detailed view icon in a file dialog.
		FileDialogInfoView               = PYQT.QStyle.SP_FileDialogInfoView #The file info icon in a file dialog.
		FileDialogContentsView           = PYQT.QStyle.SP_FileDialogContentsView #The contents view icon in a file dialog.
		FileDialogListView               = PYQT.QStyle.SP_FileDialogListView #The list view icon in a file dialog.
		FileDialogBack                   = PYQT.QStyle.SP_FileDialogBack #The back arrow in a file dialog.
		DockWidgetCloseButton            = PYQT.QStyle.SP_DockWidgetCloseButton #Close button on dock windows (see also PySide.QtGui.QDockWidget ).
		ToolBarHorizontalExtensionButton = PYQT.QStyle.SP_ToolBarHorizontalExtensionButton #Extension button for horizontal toolbars.
		ToolBarVerticalExtensionButton   = PYQT.QStyle.SP_ToolBarVerticalExtensionButton #Extension button for vertical toolbars.
		DialogOkButton                   = PYQT.QStyle.SP_DialogOkButton #Icon for a standard OK button in a PySide.QtGui.QDialogButtonBox .
		DialogCancelButton               = PYQT.QStyle.SP_DialogCancelButton #Icon for a standard Cancel button in a PySide.QtGui.QDialogButtonBox .
		DialogHelpButton                 = PYQT.QStyle.SP_DialogHelpButton #Icon for a standard Help button in a PySide.QtGui.QDialogButtonBox .
		DialogOpenButton                 = PYQT.QStyle.SP_DialogOpenButton #Icon for a standard Open button in a PySide.QtGui.QDialogButtonBox .
		DialogSaveButton                 = PYQT.QStyle.SP_DialogSaveButton #Icon for a standard Save button in a PySide.QtGui.QDialogButtonBox .
		DialogCloseButton                = PYQT.QStyle.SP_DialogCloseButton #Icon for a standard Close button in a PySide.QtGui.QDialogButtonBox .
		DialogApplyButton                = PYQT.QStyle.SP_DialogApplyButton #Icon for a standard Apply button in a PySide.QtGui.QDialogButtonBox .
		DialogResetButton                = PYQT.QStyle.SP_DialogResetButton #Icon for a standard Reset button in a PySide.QtGui.QDialogButtonBox .
		DialogDiscardButton              = PYQT.QStyle.SP_DialogDiscardButton #Icon for a standard Discard button in a PySide.QtGui.QDialogButtonBox .
		DialogYesButton                  = PYQT.QStyle.SP_DialogYesButton #Icon for a standard Yes button in a PySide.QtGui.QDialogButtonBox .
		DialogNoButton                   = PYQT.QStyle.SP_DialogNoButton #Icon for a standard No button in a PySide.QtGui.QDialogButtonBox .
		ArrowUp                          = PYQT.QStyle.SP_ArrowUp #Icon arrow pointing up.
		ArrowDown                        = PYQT.QStyle.SP_ArrowDown #Icon arrow pointing down.
		ArrowLeft                        = PYQT.QStyle.SP_ArrowLeft #Icon arrow pointing left.
		ArrowRight                       = PYQT.QStyle.SP_ArrowRight #Icon arrow pointing right.
		ArrowBack                        = PYQT.QStyle.SP_ArrowBack #Equivalent to SP_ArrowLeft when the current layout direction is Qt.LeftToRight , otherwise SP_ArrowRight .
		ArrowForward                     = PYQT.QStyle.SP_ArrowForward #Equivalent to SP_ArrowRight when the current layout direction is Qt.LeftToRight , otherwise SP_ArrowLeft .
		CommandLink                      = PYQT.QStyle.SP_CommandLink #Icon used to indicate a Vista style command link glyph.
		VistaShield                      = PYQT.QStyle.SP_VistaShield #Icon used to indicate UAC prompts on Windows Vista. This will return a null pixmap or icon on all other platforms.
		BrowserReload                    = PYQT.QStyle.SP_BrowserReload #Icon indicating that the current page should be reloaded.
		BrowserStop                      = PYQT.QStyle.SP_BrowserStop #Icon indicating that the page loading should stop.
		MediaPlay                        = PYQT.QStyle.SP_MediaPlay #Icon indicating that media should begin playback.
		MediaStop                        = PYQT.QStyle.SP_MediaStop #Icon indicating that media should stop playback.
		MediaPause                       = PYQT.QStyle.SP_MediaPause #Icon indicating that media should pause playback.
		MediaSkipForward                 = PYQT.QStyle.SP_MediaSkipForward #Icon indicating that media should skip forward.
		MediaSkipBackward                = PYQT.QStyle.SP_MediaSkipBackward #Icon indicating that media should skip backward.
		MediaSeekForward                 = PYQT.QStyle.SP_MediaSeekForward #Icon indicating that media should seek forward.
		MediaSeekBackward                = PYQT.QStyle.SP_MediaSeekBackward #Icon indicating that media should seek backward.
		MediaVolume                      = PYQT.QStyle.SP_MediaVolume #Icon indicating a volume control.
		MediaVolumeMuted                 = PYQT.QStyle.SP_MediaVolumeMuted #Icon indicating a muted volume control.
		CustomBase                       = PYQT.QStyle.SP_CustomBase #Base value for custom standard pixmaps; custom values must be greater than this value.
	########################################################################
	class ControlElement:
		PushButton            = PYQT.QStyle.CE_PushButton #A PySide.QtGui.QPushButton , draws CE_PushButtonBevel , CE_PushButtonLabel and PE_FrameFocusRect .
		PushButtonBevel       = PYQT.QStyle.CE_PushButtonBevel #The bevel and default indicator of a PySide.QtGui.QPushButton .
		PushButtonLabel       = PYQT.QStyle.CE_PushButtonLabel #The label (an icon with text or pixmap) of a PySide.QtGui.QPushButton .
		DockWidgetTitle       = PYQT.QStyle.CE_DockWidgetTitle #Dock window title.
		Splitter              = PYQT.QStyle.CE_Splitter #Splitter handle; see also PySide.QtGui.QSplitter .
		CheckBox              = PYQT.QStyle.CE_CheckBox #A PySide.QtGui.QCheckBox , draws a PE_IndicatorCheckBox , a CE_CheckBoxLabel and a PE_FrameFocusRect .
		CheckBoxLabel         = PYQT.QStyle.CE_CheckBoxLabel #The label (text or pixmap) of a PySide.QtGui.QCheckBox .
		RadioButton           = PYQT.QStyle.CE_RadioButton #A PySide.QtGui.QRadioButton , draws a PE_IndicatorRadioButton , a CE_RadioButtonLabel and a PE_FrameFocusRect .
		RadioButtonLabel      = PYQT.QStyle.CE_RadioButtonLabel #The label (text or pixmap) of a PySide.QtGui.QRadioButton .
		TabBarTab             = PYQT.QStyle.CE_TabBarTab #The tab and label within a PySide.QtGui.QTabBar .
		TabBarTabShape        = PYQT.QStyle.CE_TabBarTabShape #The tab shape within a tab bar.
		TabBarTabLabel        = PYQT.QStyle.CE_TabBarTabLabel #The label within a tab.
		ProgressBar           = PYQT.QStyle.CE_ProgressBar #A PySide.QtGui.QProgressBar , draws CE_ProgressBarGroove , CE_ProgressBarContents and CE_ProgressBarLabel .
		ProgressBarGroove     = PYQT.QStyle.CE_ProgressBarGroove #The groove where the progress indicator is drawn in a PySide.QtGui.QProgressBar .
		ProgressBarContents   = PYQT.QStyle.CE_ProgressBarContents #The progress indicator of a PySide.QtGui.QProgressBar .
		ProgressBarLabel      = PYQT.QStyle.CE_ProgressBarLabel #The text label of a PySide.QtGui.QProgressBar .
		ToolButtonLabel       = PYQT.QStyle.CE_ToolButtonLabel #A tool buttons label.
		MenuBarItem           = PYQT.QStyle.CE_MenuBarItem #A menu item in a PySide.QtGui.QMenuBar .
		MenuBarEmptyArea      = PYQT.QStyle.CE_MenuBarEmptyArea #The empty area of a PySide.QtGui.QMenuBar .
		MenuItem              = PYQT.QStyle.CE_MenuItem #A menu item in a PySide.QtGui.QMenu .
		MenuScroller          = PYQT.QStyle.CE_MenuScroller #Scrolling areas in a PySide.QtGui.QMenu when the style supports scrolling.
		MenuTearoff           = PYQT.QStyle.CE_MenuTearoff #A menu item representing the tear off section of a PySide.QtGui.QMenu .
		MenuEmptyArea         = PYQT.QStyle.CE_MenuEmptyArea #The area in a menu without menu items.
		MenuHMargin           = PYQT.QStyle.CE_MenuHMargin #The horizontal extra space on the left/right of a menu.
		MenuVMargin           = PYQT.QStyle.CE_MenuVMargin #The vertical extra space on the top/bottom of a menu.
		ToolBoxTab            = PYQT.QStyle.CE_ToolBoxTab #The toolboxs tab and label within a PySide.QtGui.QToolBox .
		SizeGrip              = PYQT.QStyle.CE_SizeGrip #Window resize handle; see also PySide.QtGui.QSizeGrip .
		Header                = PYQT.QStyle.CE_Header #A header.
		HeaderSection         = PYQT.QStyle.CE_HeaderSection #A header section.
		HeaderLabel           = PYQT.QStyle.CE_HeaderLabel #The headers label.
		ScrollBarAddLine      = PYQT.QStyle.CE_ScrollBarAddLine #Scroll bar line increase indicator. (i.e., scroll down); see also PySide.QtGui.QScrollBar .
		ScrollBarSubLine      = PYQT.QStyle.CE_ScrollBarSubLine #Scroll bar line decrease indicator (i.e., scroll up).
		ScrollBarAddPage      = PYQT.QStyle.CE_ScrollBarAddPage #Scolllbar page increase indicator (i.e., page down).
		ScrollBarSubPage      = PYQT.QStyle.CE_ScrollBarSubPage #Scroll bar page decrease indicator (i.e., page up).
		ScrollBarSlider       = PYQT.QStyle.CE_ScrollBarSlider #Scroll bar slider.
		ScrollBarFirst        = PYQT.QStyle.CE_ScrollBarFirst #Scroll bar first line indicator (i.e., home).
		ScrollBarLast         = PYQT.QStyle.CE_ScrollBarLast #Scroll bar last line indicator (i.e., end).
		RubberBand            = PYQT.QStyle.CE_RubberBand #Rubber band used in for example an icon view.
		FocusFrame            = PYQT.QStyle.CE_FocusFrame #Focus frame that is style controlled.
		ItemViewItem          = PYQT.QStyle.CE_ItemViewItem #An item inside an item view.
		CustomBase            = PYQT.QStyle.CE_CustomBase #Base value for custom control elements; custom values must be greater than this value.
		ComboBoxLabel         = PYQT.QStyle.CE_ComboBoxLabel #The label of a non-editable PySide.QtGui.QComboBox .
		ToolBar               = PYQT.QStyle.CE_ToolBar #A toolbar like PySide.QtGui.QToolBar .
		ToolBoxTabShape       = PYQT.QStyle.CE_ToolBoxTabShape #The toolboxs tab shape.
		ToolBoxTabLabel       = PYQT.QStyle.CE_ToolBoxTabLabel #The toolboxs tab label.
		HeaderEmptyArea       = PYQT.QStyle.CE_HeaderEmptyArea #The area of a header view where there are no header sections.
		ShapedFrame           = PYQT.QStyle.CE_ShapedFrame #The frame with the shape specified in the PySide.QtGui.QStyleOptionFrameV3 ; see
	########################################################################
	class SubControl:
		NONE                      = PYQT.QStyle.SC_None #Special value that matches no other sub control.
		ScrollBarAddLine          = PYQT.QStyle.SC_ScrollBarAddLine #Scroll bar add line (i.e., down/right arrow); see also PySide.QtGui.QScrollBar .
		ScrollBarSubLine          = PYQT.QStyle.SC_ScrollBarSubLine #Scroll bar sub line (i.e., up/left arrow).
		ScrollBarAddPage          = PYQT.QStyle.SC_ScrollBarAddPage #Scroll bar add page (i.e., page down).
		ScrollBarSubPage          = PYQT.QStyle.SC_ScrollBarSubPage #Scroll bar sub page (i.e., page up).
		ScrollBarFirst            = PYQT.QStyle.SC_ScrollBarFirst #Scroll bar first line (i.e., home).
		ScrollBarLast             = PYQT.QStyle.SC_ScrollBarLast #Scroll bar last line (i.e., end).
		ScrollBarSlider           = PYQT.QStyle.SC_ScrollBarSlider #Scroll bar slider handle.
		ScrollBarGroove           = PYQT.QStyle.SC_ScrollBarGroove #Special sub-control which contains the area in which the slider handle may move.
		SpinBoxUp                 = PYQT.QStyle.SC_SpinBoxUp #Spin widget up/increase; see also PySide.QtGui.QSpinBox .
		SpinBoxDown               = PYQT.QStyle.SC_SpinBoxDown #Spin widget down/decrease.
		SpinBoxFrame              = PYQT.QStyle.SC_SpinBoxFrame #Spin widget frame.
		SpinBoxEditField          = PYQT.QStyle.SC_SpinBoxEditField #Spin widget edit field.
		ComboBoxEditField         = PYQT.QStyle.SC_ComboBoxEditField #Combobox edit field; see also PySide.QtGui.QComboBox .
		ComboBoxArrow             = PYQT.QStyle.SC_ComboBoxArrow #Combobox arrow button.
		ComboBoxFrame             = PYQT.QStyle.SC_ComboBoxFrame #Combobox frame.
		ComboBoxListBoxPopup      = PYQT.QStyle.SC_ComboBoxListBoxPopup #The reference rectangle for the combobox popup. Used to calculate the position of the popup.
		SliderGroove              = PYQT.QStyle.SC_SliderGroove #Special sub-control which contains the area in which the slider handle may move.
		SliderHandle              = PYQT.QStyle.SC_SliderHandle #Slider handle.
		SliderTickmarks           = PYQT.QStyle.SC_SliderTickmarks #Slider tickmarks.
		ToolButton                = PYQT.QStyle.SC_ToolButton #Tool button (see also PySide.QtGui.QToolButton ).
		ToolButtonMenu            = PYQT.QStyle.SC_ToolButtonMenu #Sub-control for opening a popup menu in a tool button; see also Q3PopupMenu .
		TitleBarSysMenu           = PYQT.QStyle.SC_TitleBarSysMenu #System menu button (i.e., restore, close, etc.).
		TitleBarMinButton         = PYQT.QStyle.SC_TitleBarMinButton #Minimize button.
		TitleBarMaxButton         = PYQT.QStyle.SC_TitleBarMaxButton #Maximize button.
		TitleBarCloseButton       = PYQT.QStyle.SC_TitleBarCloseButton #Close button.
		TitleBarLabel             = PYQT.QStyle.SC_TitleBarLabel #Window title label.
		TitleBarNormalButton      = PYQT.QStyle.SC_TitleBarNormalButton #Normal (restore) button.
		TitleBarShadeButton       = PYQT.QStyle.SC_TitleBarShadeButton #Shade button.
		TitleBarUnshadeButton     = PYQT.QStyle.SC_TitleBarUnshadeButton #Unshade button.
		TitleBarContextHelpButton = PYQT.QStyle.SC_TitleBarContextHelpButton #Context Help button.
		DialHandle                = PYQT.QStyle.SC_DialHandle #The handle of the dial (i.e. what you use to control the dial).
		DialGroove                = PYQT.QStyle.SC_DialGroove #The groove for the dial.
		DialTickmarks             = PYQT.QStyle.SC_DialTickmarks #The tickmarks for the dial.
		GroupBoxFrame             = PYQT.QStyle.SC_GroupBoxFrame #The frame of a group box.
		GroupBoxLabel             = PYQT.QStyle.SC_GroupBoxLabel #The title of a group box.
		GroupBoxCheckBox          = PYQT.QStyle.SC_GroupBoxCheckBox #The optional check box of a group box.
		GroupBoxContents          = PYQT.QStyle.SC_GroupBoxContents #The group box contents.
		MdiNormalButton           = PYQT.QStyle.SC_MdiNormalButton #The normal button for a MDI subwindow in the menu bar.
		MdiMinButton              = PYQT.QStyle.SC_MdiMinButton #The minimize button for a MDI subwindow in the menu bar.
		MdiCloseButton            = PYQT.QStyle.SC_MdiCloseButton #The close button for a MDI subwindow in the menu bar.
		All                       = PYQT.QStyle.SC_All #Special value that matches all sub-controls.
	########################################################################
	class ContentsType:
		CheckBox      = PYQT.QStyle.CT_CheckBox #A check box, like PySide.QtGui.QCheckBox .
		ComboBox      = PYQT.QStyle.CT_ComboBox #A combo box, like PySide.QtGui.QComboBox .
		HeaderSection = PYQT.QStyle.CT_HeaderSection #A header section, like QHeader .
		LineEdit      = PYQT.QStyle.CT_LineEdit #A line edit, like PySide.QtGui.QLineEdit .
		Menu          = PYQT.QStyle.CT_Menu #A menu, like PySide.QtGui.QMenu .
		MenuBar       = PYQT.QStyle.CT_MenuBar #A menu bar, like PySide.QtGui.QMenuBar .
		MenuBarItem   = PYQT.QStyle.CT_MenuBarItem #A menu bar item, like the buttons in a PySide.QtGui.QMenuBar .
		MenuItem      = PYQT.QStyle.CT_MenuItem #A menu item, like QMenuItem .
		ProgressBar   = PYQT.QStyle.CT_ProgressBar #A progress bar, like PySide.QtGui.QProgressBar .
		PushButton    = PYQT.QStyle.CT_PushButton #A push button, like PySide.QtGui.QPushButton .
		RadioButton   = PYQT.QStyle.CT_RadioButton #A radio button, like PySide.QtGui.QRadioButton .
		SizeGrip      = PYQT.QStyle.CT_SizeGrip #A size grip, like PySide.QtGui.QSizeGrip .
		Slider        = PYQT.QStyle.CT_Slider #A slider, like PySide.QtGui.QSlider .
		ScrollBar     = PYQT.QStyle.CT_ScrollBar #A scroll bar, like PySide.QtGui.QScrollBar .
		SpinBox       = PYQT.QStyle.CT_SpinBox #A spin box, like PySide.QtGui.QSpinBox .
		Splitter      = PYQT.QStyle.CT_Splitter #A splitter, like PySide.QtGui.QSplitter .
		TabBarTab     = PYQT.QStyle.CT_TabBarTab #A tab on a tab bar, like PySide.QtGui.QTabBar .
		TabWidget     = PYQT.QStyle.CT_TabWidget #A tab widget, like PySide.QtGui.QTabWidget .
		ToolButton    = PYQT.QStyle.CT_ToolButton #A tool button, like PySide.QtGui.QToolButton .
		GroupBox      = PYQT.QStyle.CT_GroupBox #A group box, like PySide.QtGui.QGroupBox .
		ItemViewItem  = PYQT.QStyle.CT_ItemViewItem #An item inside an item view.
		CustomBase    = PYQT.QStyle.CT_CustomBase #Base value for custom contents types. Custom values must be greater than this value.
		MdiControls   = PYQT.QStyle.CT_MdiControls #The minimize, normal, and close button in the menu bar for a maximized MDI subwindow.
	########################################################################
	class StateFlag:
		State_None                = PYQT.QStyle.State_None #Indicates that the widget does not have a state.
		State_Active              = PYQT.QStyle.State_Active #Indicates that the widget is active.
		State_AutoRaise           = PYQT.QStyle.State_AutoRaise #Used to indicate if auto-raise appearance should be usd on a tool button.
		State_Children            = PYQT.QStyle.State_Children #Used to indicate if an item view branch has children.
		State_DownArrow           = PYQT.QStyle.State_DownArrow #Used to indicate if a down arrow should be visible on the widget.
		State_Editing             = PYQT.QStyle.State_Editing #Used to indicate if an editor is opened on the widget.
		State_Enabled             = PYQT.QStyle.State_Enabled #Used to indicate if the widget is enabled.
		State_HasFocus            = PYQT.QStyle.State_HasFocus #Used to indicate if the widget has focus.
		State_Horizontal          = PYQT.QStyle.State_Horizontal #Used to indicate if the widget is laid out horizontally, for example. a tool bar.
		State_KeyboardFocusChange = PYQT.QStyle.State_KeyboardFocusChange #Used to indicate if the focus was changed with the keyboard, e.g., tab, backtab or shortcut.
		State_MouseOver           = PYQT.QStyle.State_MouseOver #Used to indicate if the widget is under the mouse.
		State_NoChange            = PYQT.QStyle.State_NoChange #Used to indicate a tri-state checkbox.
		State_Off                 = PYQT.QStyle.State_Off #Used to indicate if the widget is not checked.
		State_On                  = PYQT.QStyle.State_On #Used to indicate if the widget is checked.
		State_Raised              = PYQT.QStyle.State_Raised #Used to indicate if a button is raised.
		State_ReadOnly            = PYQT.QStyle.State_ReadOnly #Used to indicate if a widget is read-only.
		State_Selected            = PYQT.QStyle.State_Selected #Used to indicate if a widget is selected.
		State_Item                = PYQT.QStyle.State_Item #Used by item views to indicate if a horizontal branch should be drawn.
		State_Open                = PYQT.QStyle.State_Open #Used by item views to indicate if the tree branch is open.
		State_Sibling             = PYQT.QStyle.State_Sibling #Used by item views to indicate if a vertical line needs to be drawn (for siblings).
		State_Sunken              = PYQT.QStyle.State_Sunken #Used to indicate if the widget is sunken or pressed.
		State_UpArrow             = PYQT.QStyle.State_UpArrow #Used to indicate if an up arrow should be visible on the widget.
		State_Mini                = PYQT.QStyle.State_Mini #Used to indicate a mini style Mac widget or button.
		State_Small               = PYQT.QStyle.State_Small #Used to indicate a small style Mac widget or button.
	########################################################################
	class ComplexControl:
		SpinBox     = PYQT.QStyle.CC_SpinBox #A spinbox, like PySide.QtGui.QSpinBox .
		ComboBox    = PYQT.QStyle.CC_ComboBox #A combobox, like PySide.QtGui.QComboBox .
		ScrollBar   = PYQT.QStyle.CC_ScrollBar #A scroll bar, like PySide.QtGui.QScrollBar .
		Slider      = PYQT.QStyle.CC_Slider #A slider, like PySide.QtGui.QSlider .
		ToolButton  = PYQT.QStyle.CC_ToolButton #A tool button, like PySide.QtGui.QToolButton .
		TitleBar    = PYQT.QStyle.CC_TitleBar #A Title bar, like those used in PySide.QtGui.QMdiSubWindow .
		GroupBox    = PYQT.QStyle.CC_GroupBox #A group box, like PySide.QtGui.QGroupBox .
		Dial        = PYQT.QStyle.CC_Dial #A dial, like PySide.QtGui.QDial .
		MdiControls = PYQT.QStyle.CC_MdiControls #The minimize, close, and normal button in the menu bar for a maximized MDI subwindow.
		CustomBase  = PYQT.QStyle.CC_CustomBase #Base value for custom complex controls. Custom values must be greater than this value.
	########################################################################
	class SubElement:
		PushButtonContents         = PYQT.QStyle.SE_PushButtonContents #Area containing the label (icon with text or pixmap).
		PushButtonFocusRect        = PYQT.QStyle.SE_PushButtonFocusRect #Area for the focus rect (usually larger than the contents rect).
		PushButtonLayoutItem       = PYQT.QStyle.SE_PushButtonLayoutItem #Area that counts for the parent layout.
		CheckBoxIndicator          = PYQT.QStyle.SE_CheckBoxIndicator #Area for the state indicator (e.g., check mark).
		CheckBoxContents           = PYQT.QStyle.SE_CheckBoxContents #Area for the label (text or pixmap).
		CheckBoxFocusRect          = PYQT.QStyle.SE_CheckBoxFocusRect #Area for the focus indicator.
		CheckBoxClickRect          = PYQT.QStyle.SE_CheckBoxClickRect #Clickable area, defaults to SE_CheckBoxFocusRect .
		CheckBoxLayoutItem         = PYQT.QStyle.SE_CheckBoxLayoutItem #Area that counts for the parent layout.
		DateTimeEditLayoutItem     = PYQT.QStyle.SE_DateTimeEditLayoutItem #Area that counts for the parent layout.
		RadioButtonIndicator       = PYQT.QStyle.SE_RadioButtonIndicator #Area for the state indicator.
		RadioButtonContents        = PYQT.QStyle.SE_RadioButtonContents #Area for the label.
		RadioButtonFocusRect       = PYQT.QStyle.SE_RadioButtonFocusRect #Area for the focus indicator.
		RadioButtonClickRect       = PYQT.QStyle.SE_RadioButtonClickRect #Clickable area, defaults to SE_RadioButtonFocusRect .
		RadioButtonLayoutItem      = PYQT.QStyle.SE_RadioButtonLayoutItem #Area that counts for the parent layout.
		ComboBoxFocusRect          = PYQT.QStyle.SE_ComboBoxFocusRect #Area for the focus indicator.
		SliderFocusRect            = PYQT.QStyle.SE_SliderFocusRect #Area for the focus indicator.
		SliderLayoutItem           = PYQT.QStyle.SE_SliderLayoutItem #Area that counts for the parent layout.
		SpinBoxLayoutItem          = PYQT.QStyle.SE_SpinBoxLayoutItem #Area that counts for the parent layout.
		ProgressBarGroove          = PYQT.QStyle.SE_ProgressBarGroove #Area for the groove.
		ProgressBarContents        = PYQT.QStyle.SE_ProgressBarContents #Area for the progress indicator.
		ProgressBarLabel           = PYQT.QStyle.SE_ProgressBarLabel #Area for the text label.
		ProgressBarLayoutItem      = PYQT.QStyle.SE_ProgressBarLayoutItem #Area that counts for the parent layout.
		FrameContents              = PYQT.QStyle.SE_FrameContents #Area for a frames contents.
		ShapedFrameContents        = PYQT.QStyle.SE_ShapedFrameContents #Area for a frames contents using the shape in PySide.QtGui.QStyleOptionFrameV3 ; see PySide.QtGui.QFrame
		FrameLayoutItem            = PYQT.QStyle.SE_FrameLayoutItem #Area that counts for the parent layout.
		HeaderArrow                = PYQT.QStyle.SE_HeaderArrow #Area for the sort indicator for a header.
		HeaderLabel                = PYQT.QStyle.SE_HeaderLabel #Area for the label in a header.
		LabelLayoutItem            = PYQT.QStyle.SE_LabelLayoutItem #Area that counts for the parent layout.
		LineEditContents           = PYQT.QStyle.SE_LineEditContents #Area for a line edits contents.
		TabWidgetLeftCorner        = PYQT.QStyle.SE_TabWidgetLeftCorner #Area for the left corner widget in a tab widget.
		TabWidgetRightCorner       = PYQT.QStyle.SE_TabWidgetRightCorner #Area for the right corner widget in a tab widget.
		TabWidgetTabBar            = PYQT.QStyle.SE_TabWidgetTabBar #Area for the tab bar widget in a tab widget.
		TabWidgetTabContents       = PYQT.QStyle.SE_TabWidgetTabContents #Area for the contents of the tab widget.
		TabWidgetTabPane           = PYQT.QStyle.SE_TabWidgetTabPane #Area for the pane of a tab widget.
		TabWidgetLayoutItem        = PYQT.QStyle.SE_TabWidgetLayoutItem #Area that counts for the parent layout.
		ToolBoxTabContents         = PYQT.QStyle.SE_ToolBoxTabContents #Area for a toolbox tabs icon and label.
		ToolButtonLayoutItem       = PYQT.QStyle.SE_ToolButtonLayoutItem #Area that counts for the parent layout.
		ItemViewItemCheckIndicator = PYQT.QStyle.SE_ItemViewItemCheckIndicator #Area for a view items check mark.
		TabBarTearIndicator        = PYQT.QStyle.SE_TabBarTearIndicator #Area for the tear indicator on a tab bar with scroll arrows.
		TreeViewDisclosureItem     = PYQT.QStyle.SE_TreeViewDisclosureItem #Area for the actual disclosure item in a tree branch.
		DialogButtonBoxLayoutItem  = PYQT.QStyle.SE_DialogButtonBoxLayoutItem #Area that counts for the parent layout.
		GroupBoxLayoutItem         = PYQT.QStyle.SE_GroupBoxLayoutItem #Area that counts for the parent layout.
		CustomBase                 = PYQT.QStyle.SE_CustomBase #Base value for custom sub-elements. Custom values must be greater than this value.
		DockWidgetFloatButton      = PYQT.QStyle.SE_DockWidgetFloatButton #The float button of a dock widget.
		DockWidgetTitleBarText     = PYQT.QStyle.SE_DockWidgetTitleBarText #The text bounds of the dock widgets title.
		DockWidgetCloseButton      = PYQT.QStyle.SE_DockWidgetCloseButton #The close button of a dock widget.
		DockWidgetIcon             = PYQT.QStyle.SE_DockWidgetIcon #The icon of a dock widget.
		ComboBoxLayoutItem         = PYQT.QStyle.SE_ComboBoxLayoutItem #Area that counts for the parent layout.
		ItemViewItemDecoration     = PYQT.QStyle.SE_ItemViewItemDecoration #Area for a view items decoration (icon).
		ItemViewItemText           = PYQT.QStyle.SE_ItemViewItemText #Area for a view items text.
		ItemViewItemFocusRect      = PYQT.QStyle.SE_ItemViewItemFocusRect #Area for a view items focus rect.
		TabBarTabLeftButton        = PYQT.QStyle.SE_TabBarTabLeftButton #Area for a widget on the left side of a tab in a tab bar.
		TabBarTabRightButton       = PYQT.QStyle.SE_TabBarTabRightButton #Area for a widget on the right side of a tab in a tab bar.
		TabBarTabText              = PYQT.QStyle.SE_TabBarTabText #Area for the text on a tab in a tab bar.
		ToolBarHandle              = PYQT.QStyle.SE_ToolBarHandle #Area for the handle of a tool bar.

########################################################################
class File_Dialog_Options:
	ShowDirsOnly                 = PYQT.QFileDialog.ShowDirsOnly          # Only show directories in the file dialog. By default both files and directories are shown. (Valid only in the Directory file mode.)
	DontResolveSymlinks          = PYQT.QFileDialog.DontResolveSymlinks   # Don't resolve symlinks in the file dialog. By default symlinks are resolved.
	DontConfirmOverwrite         = PYQT.QFileDialog.DontConfirmOverwrite  # Don't ask for confirmation if an existing file is selected. By default confirmation is requested.
	DontUseNativeDialog          = PYQT.QFileDialog.DontUseNativeDialog   # Don't use the native file dialog. By default, the native file dialog is used unless you use a subclass of PySide.QFileDialog that contains the Q_OBJECT() macro.
	ReadOnly                     = PYQT.QFileDialog.ReadOnly              # Indicates that the model is readonly.
	HideNameFilterDetails        = PYQT.QFileDialog.HideNameFilterDetails # Indicates if the file name filter details are hidden or not.
	DontUseSheet                 = PYQT.QFileDialog.DontUseSheet          # In previous versions of Qt, the static functions would create a sheet by default if the static function was given a parent. This is no longer supported and does nothing in Qt 4.5, The static functions will always be an application modal dialog. If you want to use sheets, use QFileDialog.open() instead.

########################################################################
class ItemDataRole:
	""""""
	## The general purpose roles (and the associated types):
	DISPLAY        = PYQT.Qt.DisplayRole       ## The key data to be rendered in the form of text.                                                :: QtCore.QString
	DECORATION     = PYQT.Qt.DecorationRole    ## The data to be rendered as a decoration in the form of an icon.                                 :: QColor | QIcon | QtGui.QPixmap
	EDIT           = PYQT.Qt.EditRole          ## The data in a form suitable for editing in an editor.                                           :: QString
	TOOLTIP        = PYQT.Qt.ToolTipRole       ## The data displayed in the item's tooltip.                                                       :: QtCore.QString
	STATUSTIP      = PYQT.Qt.StatusTipRole     ## The data displayed in the status bar.                                                           :: QtCore.QString
	WHATSTHIS      = PYQT.Qt.WhatsThisRole     ## The data displayed for the item in What's This? mode.                                           :: QtCore.QString
	SIZEHINT       = PYQT.Qt.SizeHintRole      ## The size hint for the item that will be supplied to views.                                      :: QtCore.QSize
	DP_ED          = [DISPLAY,EDIT]

	##Roles describing appearance and meta data (with associated types):

	FONT           = PYQT.Qt.FontRole          ## The font used for items rendered with the default delegate.                                     :: QtGui.QFont
	TEXT_ALIGNMENT = PYQT.Qt.TextAlignmentRole ## The alignment of the text for items rendered with the default delegate.                         :: Qt.AlignmentFlag
	BACKGROUND     = PYQT.Qt.BackgroundRole    ## The background brush used for items rendered with the default delegate.                         :: QtGui.QBrush
	FOREGROUND     = PYQT.Qt.ForegroundRole    ## The foreground brush (text color, typically) used for items rendered with the default delegate. :: QtGui.QBrush
	CHECKSTATE     = PYQT.Qt.CheckStateRole    ## This role is used to obtain the checked state of an item.                                       :: Qt.CheckState
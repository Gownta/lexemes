# ANSI escape codes

Sequences
ESC - sequence starting with ESC (\x1B)
CSI - Control Sequence Introducer: sequence starting with ESC [ or CSI (\x9B)
DCS - Device Control String: sequence starting with ESC P or DCS (\x90)
OSC - Operating System Command: sequence starting with ESC ] or OSC (\x9D)

General ASCII Codes
Name	decimal	octal	hex	C-escape	Ctrl-Key	Description
BEL	7	007	0x07	\a	^G	Terminal bell
BS	8	010	0x08	\b	^H	Backspace
HT	9	011	0x09	\t	^I	Horizontal TAB
LF	10	012	0x0A	\n	^J	Linefeed (newline)
VT	11	013	0x0B	\v	^K	Vertical TAB
FF	12	014	0x0C	\f	^L	Formfeed (also: New page NP)
CR	13	015	0x0D	\r	^M	Carriage return
ESC	27	033	0x1B	\e*	^[	Escape character
DEL	127	177	0x7F	<none>	<none>	Delete character

Cursor Controls
ESC Code Sequence	Description
ESC[H	moves cursor to home position (0, 0)
ESC[{line};{column}H
ESC[{line};{column}f	moves cursor to line #, column #
ESC[#A	moves cursor up # lines
ESC[#B	moves cursor down # lines
ESC[#C	moves cursor right # columns
ESC[#D	moves cursor left # columns
ESC[#E	moves cursor to beginning of next line, # lines down
ESC[#F	moves cursor to beginning of previous line, # lines up
ESC[#G	moves cursor to column #
ESC[6n	request cursor position (reports as ESC[#;#R)
ESC M	moves cursor one line up, scrolling if needed
ESC 7	save cursor position (DEC)
ESC 8	restores the cursor to the last saved position (DEC)
ESC[s	save cursor position (SCO)
ESC[u	restores the cursor to the last saved position (SCO)

Erase Functions
ESC Code Sequence	Description
ESC[J	erase in display (same as ESC[0J)
ESC[0J	erase from cursor until end of screen
ESC[1J	erase from cursor to beginning of screen
ESC[2J	erase entire screen
ESC[3J	erase saved lines
ESC[K	erase in line (same as ESC[0K)
ESC[0K	erase from cursor to end of line
ESC[1K	erase start of line to the cursor
ESC[2K	erase the entire line

Colors / Graphics Mode
ESC Code Sequence	Reset Sequence	Description
ESC[1;34;{...}m		Set graphics modes for cell, separated by semicolon (;).
ESC[0m		reset all modes (styles and colors)
ESC[1m	ESC[22m	set bold mode.
ESC[2m	ESC[22m	set dim/faint mode.
ESC[3m	ESC[23m	set italic mode.
ESC[4m	ESC[24m	set underline mode.
ESC[5m	ESC[25m	set blinking mode
ESC[7m	ESC[27m	set inverse/reverse mode
ESC[8m	ESC[28m	set hidden/invisible mode
ESC[9m	ESC[29m	set strikethrough mode.

256-color
ESC Code Sequence	Description
ESC[38;5;{ID}m	Set foreground color.
ESC[48;5;{ID}m	Set background color.

TrueColor
ESC Code Sequence	Description
ESC[38;2;{r};{g};{b}m	Set foreground color as RGB.
ESC[48;2;{r};{g};{b}m	Set background color as RGB.

Common Private Modes
These are some examples of private modes, which are not defined by the specification, but are implemented in most terminals.
ESC Code Sequence	Description
ESC[?25l	make cursor invisible
ESC[?25h	make cursor visible
ESC[?47l	restore screen
ESC[?47h	save screen
ESC[?1049h	enables the alternative buffer
ESC[?1049l	disables the alternative buffer

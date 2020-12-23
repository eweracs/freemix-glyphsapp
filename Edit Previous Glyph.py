#MenuTitle: Edit Previous Glyph
# encoding: utf-8

# by Tim Ahrens
# http://justanotherfoundry.com
# https://github.com/justanotherfoundry/glyphsapp-scripts

__doc__="""
Activates the previous glyph in the tab for editing. You can give it a keyboard shortcut in the macOS system preferences.
"""

font = Glyphs.font
initialCursor = font.currentTab.textCursor
while 1:
	font.currentTab.textCursor = (font.currentTab.textCursor - 1) % len(font.currentTab.layers)
	# in case there are no real glyphs in the tab, we need to prevent an infinite loop
	if font.currentTab.textCursor == initialCursor:
		break
	try:
		if Glyphs.font.selectedLayers[0].parent.name:
			break
	except:
		# this happens when the cursor reaches a line break
		pass

layer = Glyphs.font.selectedLayers[0]
tab = Glyphs.font.currentTab
if tab.viewPort.origin.x > tab.bounds.origin.x:
	vp = tab.viewPort
	vp.origin.x = tab.selectedLayerOrigin.x + 0.5 * ( layer.width * tab.scale - vp.size.width )
	tab.viewPort = vp

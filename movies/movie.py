import wnutils.xml as wx

my_xml = wx.Xml('rp_lum_01.xml')

my_xml.make_network_abundances_movie('rp_lum_01.mp4', 
    xlim = [0,80],
    ylim = [0,50],
    imParams = {'vmin': 1.e-25}
)

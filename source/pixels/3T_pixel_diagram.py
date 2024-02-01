import schemdraw
from schemdraw import elements as elm

with schemdraw.Drawing() as d:
    d.config(unit=2)
    elm.Ground()
    pd = elm.Photodiode().up().label('PD', loc='bottom')
    elm.Dot()
    elm.Line().up(0.45)

    QRST = elm.AnalogNFet(offset_gate=False, arrow=False).theta(180).label('RST')
    elm.Vdd().label('VRST')

    sn = elm.Line().right(0.75).at(pd.end).label('SN', ofst=(0.2,0.1))

    QSF = elm.AnalogNFet(offset_gate=False, arrow=False).theta(180).anchor('gate').at(sn.end).label('MSF', loc='right')
    elm.Line().up(1.25)
    elm.Vdd().label('VSF')


    elm.Line().down(0.5).at(QSF.drain)
    elm.Line().right(0.75)
    QREAD = elm.AnalogNFet(offset_gate=False, arrow=False).theta(90).label('READ', loc='right')
    elm.Line().right(0.5)
    read_col = elm.Dot()

    down = elm.Line().down(1).at(read_col.start).label('VOUT', loc='bottom', ofst=(0.2,0.2))
    out = elm.Line().up(4.5).label('Shared\nColumn ', loc='right')
    elm.SourceI().down().at(down.end).label('Current sink\noutside array')
    elm.Ground()



# Uncomment to run script as a check
# d.draw()


import schemdraw
from schemdraw import elements as elm
schemdraw.config(bgcolor='#FCFCFC')

with schemdraw.Drawing() as d:
    d.config(unit=2)
    elm.Ground()
    pd = elm.Photodiode().up().label('PD', loc='bottom')
    elm.Line().right(0.1)

    QTX = elm.AnalogNFet(offset_gate=False, arrow=False).theta(90).label('TX', loc='right')
    sn = elm.Line().right(0.6).label('SN', ofst=(-0.2,0.1))

    elm.Dot()
    elm.Line().up(1)

    QRST = elm.AnalogNFet(offset_gate=False, arrow=False).theta(180).label('RST')
    elm.Vdd().label('VRST')

    # sn = elm.Line().right(0.75).at(pd.end).label('SN', ofst=(0.2,0.1))
    elm.Line().right(0.75).at(sn.end)
    QSF = elm.AnalogNFet(offset_gate=False, arrow=False).theta(180).anchor('gate').label('MSF', loc='right')
    elm.Line().up(1.8)
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

    elm.Dot().at(down.end)
    elm.Line().right(1.75)
    elm.Tag().right().label('ADC')



# Uncomment to run as a script and display the result
# d.draw()


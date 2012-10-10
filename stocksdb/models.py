#!/usr/bin/env python

from database import StocksDBManager

class Symbol(Base):
    """
    Stock Symbols Table Model
    """
    __tablename__ = 'Symbols'
    
    Ticker = Column(String(5), primary_key=True)
    Name = Column(String(128))
    Exchange = Column(String(50))
    Sector = Column(String(50))
    Industry = Column(String(50))
    Quotes = relationship('Quote')

    def __init__(self, Ticker, Name, Exchange=None, Sector=None, Industry=None):
        self.Ticker = Ticker
        self.Name = Name
        self.Exchange = Exchange
        self.Sector = Sector
        self.Industry = Industry

    def __repr__(self):
        return "<Symbol('%s','%s','%s','%s','%s')>" % \
            (self.Ticker, self.Name, self.Exchange, self.Sector, self.Industry)



class Quote(Base):
    """
    Stock Quotes Table Model
    """
    __tablename__ = 'Quotes'
    
    Id = Column(Integer, primary_key=True)
    Ticker = Column(String(5), ForeignKey('Symbols.Ticker'))
    Date = Column(Date)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Float)

    def __init__(self, Ticker, Date, Open, High, Low, Close, Volume):
        self.Ticker = Ticker
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.Volume = Volume

    def __repr__(self):
        return "<Quote('%s','%s','%f','%f','%f','%f','%f')>" % \
            (self.Date, self.Ticker, self.Open, self.High, self.Low,
            self.Close, self.Volume)






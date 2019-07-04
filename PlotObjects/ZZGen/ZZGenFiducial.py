info = {  
    "Genyield": {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1,
             "xmin": 0,
             "xmax": 10
        },
        "Attributes": {  
            "GetYaxis().SetTitle": "Gen Events Passing Selection"
              }
    },
   "GenLepPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 14,
            "xmin": 0,
            "xmax": 210
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 15 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },

    "CosTheta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": -1,
            "xmax": 1
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "cos theta",  
            "GetYaxis().SetTitle": "Events/0.1",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "GenZ1Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 12,
            "xmin": 0,
            "xmax": 300
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Z_{1} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "GenZ2Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 12,
            "xmin": 0,
            "xmax": 300
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Z_{2} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "GenZPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 24,
            "xmin": 0,
            "xmax": 600
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Z p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
  "GenZMass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen m_{Z} [GeV]",  
            "GetYaxis().SetTitle": "Z bosons / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "GenZ1Mass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen m_{Z_{1}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "GenZ2Mass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen m_{Z_{2}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "GenMass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins":22,
            "xmin": 100,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen m_{4l} [GeV]",  
            "GetYaxis().SetTitle": "Events / 50 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "GenZZPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 48,
            "xmin": 0,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen ZZ p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
    "GenZ1Energy": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 48,
            "xmin": 0,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Z1 Energy [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
"GenZ2Energy": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 48,
            "xmin": 0,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Z2 Energy [GeV]",  
            "GetYaxis().SetTitle": "Events / 25 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
 "GenZ1Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 12,
            "xmin": -6,
            "xmax": 6
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen |#eta|_{Z1}",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
 "GenZ2Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 12,
            "xmin": -6,
            "xmax": 6
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen |#eta|_{Z2}",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "GenZZEta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 6,
            "xmin": 0,
            "xmax": 6
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen |#eta|_{ZZ}",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    }
}


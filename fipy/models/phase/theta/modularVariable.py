#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  PyFiVol - Python-based finite volume PDE solver
 # 
 #  FILE: "modularVariable.py"
 #                                    created: 12/8/03 {5:47:27 PM} 
 #                                last update: 1/16/04 {9:20:28 PM} 
 #  Author: Jonathan Guyer
 #  E-mail: guyer@nist.gov
 #  Author: Daniel Wheeler
 #  E-mail: daniel.wheeler@nist.gov
 #    mail: NIST
 #     www: http://ctcms.nist.gov
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  PFM is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  See the file "license.terms" for information on usage and  redistribution
 #  of this file, and for a DISCLAIMER OF ALL WARRANTIES.
 #  
 # ###################################################################
 ##

import Numeric

from fivol.variables.cellVariable import CellVariable
from fivol.variables.cellGradVariable import CellGradVariable
from fivol.variables.cellToFaceVariable import CellToFaceVariable
from fivol.variables.faceGradVariable import FaceGradVariable
from fivol.variables.faceGradVariable import FaceGradVariable

class ModularVariable(CellVariable):
    def __init__(self, mesh, name = '', value=0., unit = None, hasOld = 1):
	CellVariable.__init__(self, mesh = mesh, name = name, value = value, unit = unit, hasOld = hasOld)

        self.mod = lambda array, pi=Numeric.pi: (array + 3. * pi) % (2 * pi) - pi

    def getGrad(self):
	if self.grad is None:
	    gridSpacing = self.mesh.getMeshSpacing()
	    self.grad = self.mod(CellGradVariable(self) * gridSpacing) / gridSpacing 
	
	return self.grad

    def getFaceValue(self):
	if self.faceValue is None:
	    self.faceValue = CellToFaceVariable(self, self.mod)

	return self.faceValue

    def getFaceGrad(self):
	if self.faceGrad is None:
	    self.faceGrad = FaceGradVariable(self, self.mod)

	return self.faceGrad

    def getFaceGradNoMod(self):
        if self.faceGrad is None:
	    self.faceGrad = FaceGradVariable(self)

	return self.faceGrad
    
    def updateOld(self):
        if self.old != None:
            self.value = self.mod(self.value)
	    self.old.setValue(self.value)
    
	



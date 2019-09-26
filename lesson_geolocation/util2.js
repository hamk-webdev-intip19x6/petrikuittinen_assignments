var myutil= {
    INCH_IN_CM : 2.54,
    inchesToCm : function (inch) {
	return inch*this.INCH_IN_CM;
    },
    cmToInches : function (cm) {
	return cm/this.INCH_IN_CM;
    }
};


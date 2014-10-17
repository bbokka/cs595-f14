all:
	pdflatex A5_Report.tex
	bibtex A5_Report.aux	
	pdflatex A5_Report.tex
	pdflatex A5_Report.tex
	mv A5_Report.pdf A5_Report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

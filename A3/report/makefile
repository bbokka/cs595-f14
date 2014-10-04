all:
	pdflatex A3-report.tex
	bibtex A3-report.aux	
	pdflatex A3-report.tex
	pdflatex A3-report.tex
	mv A3-report.pdf A3-report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

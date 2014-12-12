all:
	pdflatex A10-report.tex
	bibtex A10-report.aux	
	pdflatex A10-report.tex
	pdflatex A10-report.tex
	mv A10-report.pdf A10-report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

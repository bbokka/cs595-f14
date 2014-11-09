all:
	pdflatex A7_report.tex
	bibtex A7_report.aux	
	pdflatex A7_report.tex
	pdflatex A7_report.tex
	mv A7_report.pdf A7_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

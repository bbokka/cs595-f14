all:
	pdflatex A9_report.tex
	bibtex A9_report.aux	
	pdflatex A9_report.tex
	pdflatex A9_report.tex
	mv A9_report.pdf A9_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

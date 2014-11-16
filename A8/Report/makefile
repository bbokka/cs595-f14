all:
	pdflatex A8_report.tex
	bibtex A8_report.aux	
	pdflatex A8_report.tex
	pdflatex A8_report.tex
	mv A8_report.pdf A8_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

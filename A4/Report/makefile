all:
	pdflatex A4_report.tex
	bibtex A4_report.aux	
	pdflatex A4_report.tex
	pdflatex A4_report.tex
	mv A4_report.pdf A4_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

all:
	pdflatex A2_report.tex
	bibtex A2_report.aux	
	pdflatex A2_report.tex
	pdflatex A2_report.tex
	mv A2_report.pdf A2_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

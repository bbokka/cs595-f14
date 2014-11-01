all:
	pdflatex A6_report.tex
	bibtex A6_report.aux	
	pdflatex A6_report.tex
	pdflatex A6_report.tex
	mv A6_report.pdf A6_report_bbokka.pdf
clean:
	rm -v *.aux *.toc *.log *.bbl *.out

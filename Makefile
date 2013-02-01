
all: *.tex
	pdflatex thesis.tex
	pdflatex thesis.tex

clean:
	-rm *.aux *.lof *.log *.lot *.pdf *.toc
	

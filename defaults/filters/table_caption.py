"""
An alteration to @lhoupert's answer

https://github.com/jgm/pandoc/issues/1023#issuecomment-797435932

Which is based on:

https://github.com/jgm/pandoc/issues/1023#issuecomment-656769330

"""
import pandocfilters as pf
from pandocfilters import walk

def return_latex_ref(x):
    result = []

    def go(key, val, format, meta):
        if key in 'RawInline':
            """ Commented out from original code to allow inline styling of caption labels
            """
            #if val[0] == 'tex' and '\\label' in val[1]:
            #  result.append(val[1])
          
            # Allows styling to caption text
            result.append(val[1])

    walk(x, go, "", {})
    return ''.join(result)

def tabular(key, value, format, meta):

  if key == 'Table' and 'processed' not in value[0][1]:
    caption = value[1]
    cap = pf.stringify(caption) + ' ' + return_latex_ref(caption)

    cmd = f'\\renewcommand\\tcap{{{cap}}}'

    value[0][1].append('processed')
    value[1] = [None, []]
    mytable = pf.elt('Table', len(value))
    
    return [pf.RawBlock('latex', cmd), mytable(*value)]

if __name__ == '__main__':
  pf.toJSONFilter(tabular)
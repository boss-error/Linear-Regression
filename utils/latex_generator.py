def generate_latex_output(results):
    """Generate LaTeX formatted output for the calculations"""
    n = len(results['x'])  # Ensure 'n' is the number of data points
    
    table_latex = f"""
    \\[
    \\begin{{array}}{{|c|c|c|c|c|}}
    \\hline
    x & y & x^2 & y^2 & x \\cdot y \\\\
    \\hline
    """
    
    for i in range(n):
        table_latex += f"{results['x'][i]} & {results['y'][i]} & {results['x_sq'][i]} & {results['y_sq'][i]} & {results['x_y'][i]} \\\\ \n"
    
    table_latex += f"""
    \\hline
    \\text{{Sum}} & \\text{{Sum}} & \\text{{Sum}} & \\text{{Sum}} & \\text{{Sum}} \\\\
    \\hline
    {results['sum_x']} & {results['sum_y']} & {results['sum_x_sq']} & {results['sum_y_sq']} & {results['sum_x_y']} \\\\
    \\hline
    \\end{{array}}
    \\]
    """
    
    equations_latex = f"""
    \\[
    a = \\frac{{n \\cdot \\sum(xy) - \\sum(x) \\cdot \\sum(y)}}{{n \\cdot \\sum(x^2) - (\\sum(x))^2}}
    \\]
    \\[
    b = \\frac{{\\sum(y) - a \\cdot \\sum(x)}}{n}
    \\]
    """
    
    steps_latex = f"""
    \\[
    a = \\frac{{{n} \\cdot {results['sum_x_y']} - {results['sum_x']} \\cdot {results['sum_y']}}}
         {{{n} \\cdot {results['sum_x_sq']} - ({results['sum_x']})^2}}
    = {results['a']:.4f}
    \\]
    \\[
    b = \\frac{{{results['sum_y']} - ({results['a']:.4f}) \\cdot {results['sum_x']}}}
         {{{n}}}
    = {results['b']:.4f}
    \\]
    """
    
    result_latex = f"""
    \\[
    y = {results['a']:.4f}x + {results['b']:.4f}
    \\]
    \\[
    \\text{{At }} x = {results['predict_value']}:
    \\]
    \\[
    y = {results['a']:.4f} \\cdot {results['predict_value']} + {results['b']:.4f}
    = {results['predicted_y']:.4f}
    \\]
    """
    
    return table_latex, equations_latex, steps_latex, result_latex

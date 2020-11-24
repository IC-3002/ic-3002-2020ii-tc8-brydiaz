def contar_rutas_mas_cortas(C):

    limite = len(C)-1
    if  C[limite][limite] == 1:
        return 0
    else:
        C[limite][limite] = 'y'
        return verificarMatrizColumna(C, limite, 1, 0, 0) +1
        



def verificarMatrizColumna(C, limite, i, posiblesRutas, iteraciones):

    if limite != -1:

        if limite == len(C)-1:

            if i> len(C)-1:
                if C[i-1][limite] == 'y':
                    return verificarMatrizColumna(C, limite-1, 1 , posiblesRutas+1, iteraciones+1 )
            
                elif C[i-1][limite] == 0:
                    C[i-1][limite] = 'b'
                    return verificarMatrizColumna(C, limite, i+1, posiblesRutas, iteraciones )
                else:
                    return verificarMatrizColumna(C, limite-1, 1 , posiblesRutas, iteraciones+1)

            elif C[i][limite] == 'y':
                return verificarMatrizColumna(C, limite-1, 1 , posiblesRutas+1, iteraciones+1 )
            
            elif C[i][limite] == 0:
                C[i][limite] = 'b'
                return verificarMatrizColumna(C, limite, i+1, posiblesRutas, iteraciones )
            else:
                return verificarMatrizColumna(C, limite-1, posiblesRutas, iteraciones+1)
        elif i <= len(C)-1:

            if C[i][limite] == 0:
                if C[i][limite+1] == 'b':
                    C[i][limite] = 'b'
                    return verificarMatrizColumna(C, limite, i+1, posiblesRutas+1*iteraciones, iteraciones)

                elif C[i][limite+1] == 'y':
                    C[i][limite] = 'b'
                    return verificarMatrizColumna(C, limite-1, 1, posiblesRutas+1*iteraciones, iteraciones+1)
                else:
                    return verificarMatrizColumna(C, limite-1, 1, posiblesRutas, iteraciones+1)
            else:
                return verificarMatrizColumna(C, limite-1, 1, posiblesRutas, iteraciones+1)
        else:
            return verificarMatrizColumna(C, limite-1, 1, posiblesRutas, iteraciones+1)

    else:
        return posiblesRutas




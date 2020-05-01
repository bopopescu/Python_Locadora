USE BD_LOCADORA;
DROP FUNCTION VALIDAR_CPF_F;
DELIMITER $$;
CREATE FUNCTION VALIDAR_CPF_F(CPF CHAR(14)) RETURNS DOUBLE
BEGIN
    DECLARE INDICE INT;
    DECLARE SOMA INT;
    DECLARE DIG1 INT;
    DECLARE DIG2 INT;
    DECLARE CPF_TEMP VARCHAR(11);
    DECLARE DIGITOS_IGUAIS CHAR(1);
    DECLARE RESULTADO CHAR(1);

    SET RESULTADO = FALSE;

    /*
    Verificando se os dígitos são iguais
    */

    SET CPF_TEMP = SUBSTRING(CPF,1,1);

    SET INDICE = 1;
    SET DIGITOS_IGUAIS = 'S';

  IF (LENGTH(CPF)>11) THEN
    SET DIGITOS_IGUAIS = 'S';
  ELSE
    SET DIG1=LENGTH(CPF);
    WHILE (DIG1<=12) DO
      SET CPF=CONCAT("0",CPF);
      SET DIG1=DIG1+1;
    END WHILE;
    SET CPF=RIGHT(CPF,11);
      WHILE (INDICE <= 11) DO
          IF (SUBSTRING(CPF,INDICE,1) <> CPF_TEMP) Then
              SET DIGITOS_IGUAIS = 'N';
          END IF;
          SET INDICE = INDICE + 1;
      END WHILE;
  END IF;

    /*Caso os dígitos não sejam todos iguais Começo o calculo do dígitos*/
    IF (DIGITOS_IGUAIS = 'N') THEN
        /*Cálculo do 1º dígito*/
        SET SOMA = 0;
        SET INDICE = 1;
        WHILE (INDICE <= 9) DO          
            SET Soma = Soma + CAST(SUBSTRING(CPF,INDICE,1) AS UNSIGNED) * (11 - INDICE);             SET INDICE = INDICE + 1;      
         END WHILE;      
         SET DIG1 = 11 - (SOMA % 11);      
         IF (DIG1 > 9) THEN
            SET DIG1 = 0;
         END IF;

        -- Cálculo do 2º dígito }
        SET SOMA = 0;
        SET INDICE = 1;
        WHILE (INDICE <= 10) DO
             SET Soma = Soma + CAST(SUBSTRING(CPF,INDICE,1) AS UNSIGNED) * (12 - INDICE);              
             SET INDICE = INDICE + 1;
        END WHILE;
        SET DIG2 = 11 - (SOMA % 11);
        IF DIG2 > 9 THEN
            SET DIG2 = 0;
        END IF;

        -- Validando
        IF (DIG1 = SUBSTRING(CPF,LENGTH(CPF)-1,1)) AND (DIG2 = SUBSTRING(CPF,LENGTH(CPF),1)) THEN
            SET RESULTADO = TRUE;
        ELSE
            SET RESULTADO = FALSE;
        END IF;

    END IF;
    RETURN RESULTADO;
END $$;
-- ------------------------------------------------------------------------------------------------
SELECT VALIDAR_CPF_F('26369201020');
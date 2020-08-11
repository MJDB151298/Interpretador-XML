;#lang scheme
;--------------------------------------------------------------
;CAlCULO DE CALORIAS || TOMADO DE: https://computerhoy.com/noticias/life/esta-formula-te-dice-cuantas-calorias-debes-comer-dia-adelgazar-286837
;Leyenda de opciones de actividad fisica || Calorias en reposo (multiplicar por el TMB (Tasa Metabolica Basal))
;Poco o ningún ejercicio --> TMB * 1,2
;Ejercicio ligero (1 a 3 días a la semana) --> TMB * 1,375
;Ejercicio moderado (3 a 5 días a la semana)  --> TMB * 1,55
;Deportista (6 -7 días a la semana)  --> TMB * 1,72
;Atleta (Entrenamientos mañana y tarde)  --> TMB * 1,9

;CALCULO DE TMB
;Para hombres
;TMB = 66 + (13,7 x peso en kg) + (5 x altura en cm) - (6,75 x edad en años)
(define TmbHombres
  (lambda (peso altura edad)
    (+ 66 (+ (* 13.7 peso)  (-(* 5 altura) (* 6.75 edad))))))

;Para mujeres
;TMB = 655 + (9,6 x peso en kg) + (1.8 x altura en cm) - (4,7 x edad en años)
(define TmbMujeres
  (lambda (peso altura edad)
   (+ 655 (+ (* 9.6 peso)  (-(* 1.8 altura) (* 4.7 edad)))) ))

;Calcular TMB |OPCIONES :| Hombre = 1 || Mujer = 2
(define calcularTMB
  (lambda (opcionSexo peso altura edad)
    (cond [(= opcionSexo 1) (TmbHombres peso altura edad)]
          [else  (TmbMujeres peso altura edad) ])))

;CALCULO DE CALORIAS DIARIAS PARA CONSERVAR EL PESO ACTUAL
(define caloriasDiariasPesoActual
  (lambda (opcionActividadFisica opcionSexo peso altura edad)
    (cond [(= opcionActividadFisica 1) (* (calcularTMB opcionSexo peso altura edad) 1.2)]
          [(= opcionActividadFisica 2) (* (calcularTMB opcionSexo peso altura edad) 1.375)]
          [(= opcionActividadFisica 3) (* (calcularTMB opcionSexo peso altura edad) 1.55)]
          [(= opcionActividadFisica 4) (* (calcularTMB opcionSexo peso altura edad) 1.72)]
          [else (* (calcularTMB opcionSexo peso altura edad) 1.9) ])))

;CALCULO DE CALORIAS DIARIAS PARA DISMINUIR PESO SEGUN LO QUE SE QUIERA DISMINUIR A LA SEMANA
(define caloriasDiariasDisminuirPeso
  (lambda (opcionActividadFisica opcionSexo peso altura edad pesoDisminuirALaSemana)
    (cond [(= opcionActividadFisica 1) (- (* (calcularTMB opcionSexo peso altura edad) 1.2) (* pesoDisminuirALaSemana 1000))]
          [(= opcionActividadFisica 2) (- (* (calcularTMB opcionSexo peso altura edad) 1.375) (* pesoDisminuirALaSemana 1000))]
          [(= opcionActividadFisica 3) (- (* (calcularTMB opcionSexo peso altura edad) 1.55) (* pesoDisminuirALaSemana 1000))]
          [(= opcionActividadFisica 4) (- (* (calcularTMB opcionSexo peso altura edad) 1.72) (* pesoDisminuirALaSemana 1000))]
          [else (- (* (calcularTMB opcionSexo peso altura edad) 1.9) (* pesoDisminuirALaSemana 1000)) ])))

;--------------------------------------------------------------
(define logB
  (lambda (x base)
    (/ (log x) (log base))
))

;CALCULAR GRASA CORPORAL || Variables: medida cintura (cm), medida cuello(cm), medida altura(cm), medida cadera (cm)
;Formula grasa corporal en Hombres
;GrasaHombres = (495 / (1.0324 - ((log(cintura - cuello)) + ( 0.15456 * (log(altura)))  ) - 450) )
(define grasaHombres
  (lambda (cintura cuello altura)
     (- (/ 495 (+ (- 1.0324 (* 0.19077 (logB (- cintura cuello) 10))) (* 0.15456 (logB altura 10)))) 450) ))

;Formula grasa corporal mujeres
;GrasaMujeres = (495 / ((1.29579 - (0.35004 * ( (log(cintura + cadera + cuello)) + (0.22100 * (log(altura))) ) ) ) - 450 ) )
(define grasaMujeres
  (lambda (cintura cuello altura cadera)
    (- (/ 495 (+ (- 1.29579(* 0.35004 (logB (- (+ cintura cadera) cuello) 10))) (* 0.22100 (logB altura 10)))) 450) ))

;RANGOS DEL PORCENTAJE DE GRASA CORPORAL:
;                Mujeres     Hombres
;Grasa esencial  10-12%      2-4%
;Atleta    	 14-20%      6-13%
;Fitness 	 21-24%      14-17%
;Aceptable 	 25-31%      18-25%
;Obesidad 	 32% o más   26% o más
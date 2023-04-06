<div aling="justify">
# UC DIAGRAM:

## Indice
  - [Introduction](#introduction).
  - [Description](#description).
  - [Actors specification ](#especificación-de-actores).
  - [Especificación de casos de uso](#especificación-de-casos-de-uso).
### Introduction
This document specifies the __use case diagram__ of the __"papapa"__ system.
This document outlines the use cases identified, as well as the actors involved in them.
## Actors identification.
- Guest
- User
- Database

## Use cases identification.

- Guest:
  - Sign up
  - Play guest party mode
  - Visit store
  - Access configuration
  
- User:
  - Asociar tarjeta
  - Establecer límite del dinero
  - Realizar pedidos
  - Mostrar productos ---> Verificar Stock
  - Seleccionar productos
  - Finalizar pedido
  - Pedido compuesto

- Sistema:
  - Comprobar pedido
  - Aprobar pedido
  - Rechazar pedido
  - Cobrar pedido
  - Confirmar pedido
  - Generar orden de distribución

- Transportista
  - Entregar pedido
 
## DIAGRAMA C.U.

 <div align="center">
  </br>
  <img src="https://github.com/samugd17/Entornos-de-desarrollo/blob/921c44cd07a5c2ec97a385c147c769163f79ed6a/2%C2%AAEvaluaci%C3%B3n/TAREAS/TAREA5/IMG/Tienda_Virtual.drawio.png">
  </br>
 </div>




  
### Descripción

  Una empresa basada en una web que vende sus productos de forma digital, quiere hacer una supervisión de todos los pedidos que realizan sus clientes así como del stock de productos que posee. Para ello, se han especificado una serie de requisitos descritos en el presente documento.

### Especificación de Actores

  En el presente documento se realiza la especificación de los diferentes actores que intervienen en la solución propuesta.

#### Cliente

  |  Actor | Cliente |
  |---|---|
  | Descripción  | Cliente anónimo que accede a la web  |
  | Características  | El cliente aún no ha sido registrado y por tanto su capacidad de interacción con el sistema es muy reducida |
  | Relaciones |   |
  | Referencias | __C.U.1, C.U.2__ |   
  |  Notas |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  |Fecha | _19/01/2023_ |

#### Cliente registrado

  |  Actor | Cliente registrado |
  |---|---|
  | Descripción  | Cliente que ya se encuentra registrado en la web | |
  | Relaciones | El cliente registrado puede realizar las acciones del cliente a parte de las suyas propias  |
  | Referencias | __C.U.1, C.U.2, C.U.3, C.U.4, C.U.5, C.U.6, C.U.7, C.U.8__ |   
  |  Notas |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  |Fecha | _19/01/2023_ |

#### Sistema

  |  Actor | Sistema |
  |---|---|
  | Descripción  | Sistema automatizado que ejecuta laboras de gestión | |
  | Relaciones |  |
  | Referencias | __C.U.9, C.U.10, C.U.11, C.U.12, C.U.13, C.U.14, C.U.15, C.U.16__ |   
  |  Notas |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  |Fecha | _19/01/2023_ |

#### Transportista

  |  Actor | Transportista |
  |---|---|
  | Descripción  | Persona encargada de hacer llegar el producto a su destino | |
  | Relaciones | |
  | Referencias | __C.U.17, C.U.18__ |   
  |  Notas |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  |Fecha | _19/01/2023_ |

### Especificación de Casos de uso


#### Registrar

|  Caso de Uso	CU.1 | Registrar |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/samugd17/Entornos-de-desarrollo/tree/main/2%C2%AAEvaluaci%C3%B3n/TAREAS/TAREA5).  |
| Actor  |  Cliente |
| Descripción | El cliente se registra en el sistema. |
| Flujo básico | El cliente lleva a cabo el registro de su persona en la base de datos de la web. |
| Pre-condiciones | El cliente ha ingresado en la web y desea realizar alguna compra |  
| Post-condiciones  | El cliente debe asociar una tarjeta de crédito válida|  
|  Requerimientos | Disponer de una tarjeta de crédito/débito válida |
|  Notas |  |
| Autor  | _Samuel Eloy González Díaz_ |
|Fecha | _19/01/23_ |

</div>
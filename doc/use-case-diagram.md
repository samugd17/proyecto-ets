<div aling="justify">

# UC DIAGRAM: TABLESTARS

## Indice
  - [Introduction](#introduction).
  - [Description](#description).
  - [Actors specification ](#actors-identification).
  - [Use Cases specification](#use_cases_specification).

### Introduction
This document specifies the __use case diagram__ of the _**TableStars**_ system.
This document outlines the use cases identified, as well as the actors involved in them.

## Actors identification.
- Guest
- User
- Database

## Use cases identification.

- Guest user:
  - Sign up
  - Play guest party mode
  - Visit store
  - Access configuration
  
- User:
  - Login
  - Access real price party mode
  - Access virtual price party mode
    - Check credit card
    - Credit card approved
    - Credit card rejected
    - Play
  - Play multiplayer mode
  - Send and receive friend requests
  - Shopping at the store
  - Personalice skins
  - Access bookmarks

- Database:
  - Send data
 
## UC DIAGRAM

 <div align="center">
  </br>
  <img src="doc/img/TableStars_CU.png">
  </br>
 </div>

### Description

TableStars will be a platform to play classic tabletop games online and with a new layer of challenge.

We aim to create a tabletop gaming community that revolves around competition and betting, giving our players a selection of classic tabletop games and a wide range of tables both free and paid with different types and ammounts of bets.

### Actors specification

This document specifies the different actors involved in the proposed solution.

#### Guest user

  |  Actor | Guest user|
  |---|---|
  | Description  | guest user who will be able to perform minimal actions with the system.|
  | Relations |  |
  | References | __UC.1, UC.2, UC.3, UC.4__ |   
  | Notes |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  | Date | _06/04/2023_ |

#### Cliente registrado

  |  Actor | User|
  |---|---|
  | Description  | User that has been already registered in TableStars |
  | Relations | The registered user can perform the guest's actions in addition to his own actions. |
  | References | __UC.1, UC.2, UC.3, UC.4, UC.5, UC.6, UC.7, UC.8, UC.9, UC.10, UC.11, UC.12__ |   
  |  Notes |   |
  | Autor  | _Samuel Eloy González Díaz_ |
  | Date | _06/04/2023_ |

#### Database

  |  Actor | Database|
  |---|---|
  | Description  | Database containing all the data necessary for the proper functioning of the application.|
  | Relations | |
  | References | __UC.17__ |   
  | Notes |  |
  | Autor  | _Samuel Eloy González Díaz_ |
  | Date | _06/04/2023_ |


### Use Cases specification

#### Sign up

| UC.1 | Sign up |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md).  |
| Actor | Guest user |
| Description | The guest user can log into the system to access all available user functions.  |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | Guest user will be transform into User, so he can access all available user functions |  
| Requirements | |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Play guest party mode

| UC.2 | Play guest party mode |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | Guest user |
| Description | Free game mode where you can play against random players from all over the world |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes | It isn't neccesary an account to play in this mode. A temporary user will be created with the following sintax: _"guest1234"_ |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Visit Store

| UC.3 | Visit Store |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | Guest user |
| Description | Allows you to consult the store and view the different offers |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Basic settings

| UC.4 | Basic settings |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | Guest user |
| Description | Allows you to configure different game settings, such as language, audio, etc.  |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Log in

| UC.5 | Log in |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to identificate in the system|
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Play real price party mode

| UC.6 | Play real price party mode|
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to play using real money as a wager|
| Basic flow | 1. Log in|
|            | 2. Play real price party mode|
| Pre-conditions | Log in |  
| Post-conditions  | Check credit card|  
| Requirements | Have a valid credit card|
| Notes | This is a paymode game |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Play virtual price party mode

| UC.7 | Play virtual price party mode |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to play using virtual coins as a wager |
| Basic flow | 1. Log in|
|            | 2. Play virtual price party mode|
| Pre-conditions | Log in |  
| Post-conditions  | Check credit card|  
| Requirements | Have a valid account in the system  |
| Notes | This is a paymode game |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Play multiplayer mode

| UC.8 | Play multiplayer mode |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to have a match between your friends |
| Basic flow | 1. Log in|
|            | 2. Play multiplayer mode|
| Pre-conditions |Log in |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Send and receive friend requests

| UC.9 | Send and receive friend requests |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to add friends within the app |
| Basic flow | 1. Log in|
|            | 2. Send and receive friend requests|
| Pre-conditions |Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system  |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Shopping in the store

| UC.10 | Shopping in the store |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to buy different skins for the user avatar, board etc. You can also buy virtual game coins |
| Basic flow | 1. Log in|
|            | 2. Shopping in the store|
| Pre-conditions | Log in |  
| Post-conditions  | Check credit card|  
| Requirements | Have a valid account in the system |
| Notes | Virtual coins may be exchanged for any item in the store or may be used as a wagering item in virtual price party mode |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Personalice skins

| UC.11 | Personalice skins |
|---|---|
| Sources | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to customize the appearance of the board, dice, avatars, etc. |
| Basic flow | 1. Log in|
|            | 2. Personalice skins|
| Pre-conditions | Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Advanced settings

| UC.12 | Advanced settings |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to configure different advanced settings, such as your username, password, modify your credit card, etc. |
| Basic flow | 1. Log in|
|            | 2. Advanced settings|
| Pre-conditions | Log in |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Access bookmarks

| UC.13 | Access bookmarks |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to consult the leaderboards and high score rankings, globally and among your friends |
| Basic flow | 1. Log in|
|            | 2. Access bookmarks|
| Pre-conditions | Login|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | Bookmarks vary depending on the user |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Check credit card 

| UC.14 | Check credit card |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Verify the status of the credit card |
| Basic flow | 1. Log in |
|            | 2. Access paymode game or shop in the store  |
|            | 3. Check credit card |
| Pre-conditions | Access paymode game or shop in the store |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Credit card not exist

| UC.15 | Credit card not exist |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description |Verify that the credit card doesn't exists or is not valid.|
| Basic flow | 1. Log in |
|            | 2. Access paymode game or shop in the store  |
|            | 3. Check credit card |
|            | 4. Credit card not exist |
| Pre-conditions | Check credit card |  
| Post-conditions  | Add credit card |  
| Requirements | Have a valid account in the system |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Credit card exist

| UC.16 | Credit card exist |
|---|---|
| Sources  | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Verify that the credit card exists and is valid.|
| Basic flow | 1. Log in |
|            | 2. Access paymode game or shop in the store  |
|            | 3. Check credit card |
|            | 4. Credit card exist |
| Pre-conditions | Check credit card |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Add credit card

| UC.17 | Add credit card |
|---|---|
| Sources | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to add your credit card to be able to play all modes |
| Basic flow | 1. Log in |
|            | 2. Access paymode game |
|            | 3. Check credit card |
|            | 4. Credit card not exist |
|            | 5. Add credit card |
| Pre-conditions | The system checks that the user doesn't have a credit card linked to his account.|  
| Post-conditions  | The user will return to the main menu to be able to play all modes and shop in the store|  
| Requirements | Have a bank account|
| Notes | |
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

#### Send data

| UC.18 | Send data and receive data |
|---|---|
| Sources | The use case is supported by [this document](doc/use-case-diagram.md). |
| Actor | Database |
| Description | Send and receive necessary data for the different use cases of the system |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes | This UC is automatically done by the system|
| Autor  | _Samuel Eloy González Díaz_ |
| Date | _06/04/2023_ |

</div>
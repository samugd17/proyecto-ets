<div aling="justify">

# UC DIAGRAM: TABLESTARS
 <div align="center">
  </br>
  <img src="https://github.com/samugd17/proyecto-ets/blob/develop/doc/img/tablestars.png"/>
  </br>
 </div>

## Index
  - [Introduction](#introduction).
  - [Description](#description).
  - [Actors identification ](#actors-identification).
  - [Use Cases identification](#use-cases-identification).
  - [Use Cases Diagram](#use-cases-diagram).
  - [Actors specification](#actors-specification).
  - [Use Cases specification](#use-cases-specification).

### Introduction
This document specifies the __use case diagram__ of the _**TableStars**_ system.
This document outlines the use cases identified, as well as the actors involved in them.

### Description

TableStars will be a platform to play classic board games online and with a new layer of challenge.

Our goal is to create a board game community that revolves around competition and betting, offering our players a selection of classic games and a wide range of both free and paid tables, with different types and amounts of bets, depending on the currency used.  There will be two, virtual coins and diamonds. 

Our first game to be implemented will be Parcheesi, which will have two table sizes: 4 players, 6 players. And it will have up to 4 tables of different betting levels, in its paid game modes.

Game modes are as follows:
- _Virtual prize party_: In this mode you can bet your virtual coins.
- _Real prize party_: In this mode you can bet your diamonds.
- _Guest party_: In this mode, you can play as a guest or you can logged in with your current user and play versus random people for free.
- _Friends party_: In this mode you can play against your friends in the game.

In addition to all this, the application will have a store where you can buy different skins for the boards, dice and player tokens, and where you can exchange diamonds for virtual coins. In case of not having enough diamonds, they can also be purchased directly from the store.

## Actors identification.
- Guest
- User
- Database

## Use cases identification.

- Guest user:
  - Sign up
  - Play guest party mode
  - Visit store
  - Basic settings
  
- User:
  - Login
  - Shopping in the store
    - Buy diamonds
    - Check credit card
    - Credit card exist
    - Credit card not exist
    - Add credit card
    
  - Play virtual prize party mode
    - Select table size
    - Select stake level
    - Check enough necessary token
      - Approve operation
      - Deny operation
  - Play real prize party mode
  - Play friends party mode
    - Join game room
    - Create game room
    - Invite friends
  - Personalice skins
  - Search player
    - Send friend request
    - Consult player stats
  - Receive friend request
    - Accept friend request
    - Decline friend request
  - Advance settings
  - Consult scoreboards

- Database:
  - Send data
  - Receive data
 
## Use Cases Diagram

 <div align="center">
  </br>

  <img src="/home/usuario/Documentos/REPOSITORIOS/proyecto-ets/doc/img/TableStars_CU.png"/> 

  </br>
 </div>

### Actors specification

This document specifies the different actors involved in the proposed solution.

#### Guest user

  |  Actor | Guest user|
  |---|---|
  | Description  | Guest user who will be able to perform minimal actions with the system.|
  | Relations |  |
  | References | __UC.1, UC.2, UC.3, UC.4__ |   
  | Notes |   |
  | Autor  | _Samuel Eloy González Díaz & Jaime León_ |
  | Date | _06/04/2023_ |

#### User

  |  Actor | User|
  |---|---|
  | Description  | User that has been already registered in TableStars |
  | Relations | The registered user can perform the guest's actions in addition to his own actions. |
  | References | __UC.1, UC.2, UC.3, UC.4, UC.5, UC.6, UC.7, UC.8, UC.9, UC.10, UC.11, UC.12, UC.13, UC.14, UC.15, UC.16, UC.17, UC.22, UC.25, UC.26, UC.27, UC.28, UC.29, UC.30, UC.31__ |   
  |  Notes |   |
  | Autor  | _Samuel Eloy González Díaz & Jaime León_ |
  | Date | _06/04/2023_ |

#### Database

  |  Actor | Database|
  |---|---|
  | Description  | Database containing all the data necessary for the proper functioning of the application.|
  | Relations | |
  | References | __UC.32, UC.33__ |   
  | Notes |  |
  | Autor  | _Samuel Eloy González Díaz & Jaime León_ |
  | Date | _06/04/2023_ |


### Use Cases specification
This document specifies the different Use Cases involved in the proposed solution.

#### Sign up

| UC.1 | Sign up |
|---|---|
| Sources  | The use case is supported by [this document](#use-cases-diagram).  |
| Actor | Guest user |
| Description | The guest user can log into the system to access all available user functions.  |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | Guest user will be transform into User, so he can access all available user functions |  
| Requirements | Have a valid e-mail address |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Play guest party mode

| UC.2 | Play guest party mode |
|---|---|
| Sources  | The use case is supported by [this document](#use-cases-diagram). |
| Actor | Guest, User |
| Description | Free game mode where you can play against random players from all over the world. |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes | It isn't neccesary to have an account to play in this mode. A temporary user will be created with the following sintax: _"guest1234"_. If you are already logged into the aplication, you will play as your user. |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Visit Store

| UC.3 | Visit Store |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | Guest user |
| Description | Allows you to consult the store and view the different offers |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Basic settings

| UC.4 | Basic settings |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | Guest user |
| Description | Allows you to configure different game settings, such as language, audio, etc.  |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Log in

| UC.5 | Log in |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to identificate in the system|
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Shopping in the store

| UC.6 | Shopping in the store |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to buy different skins for the user avatar, board etc. You can also buy virtual game coins and diamonds. |
| Basic flow | 1. Log in|
|            | 2. Shopping in the store|
| Pre-conditions | Log in |  
| Post-conditions  | Check enough necessary token (Virtual coin and Diamonds)|  
| Requirements | Have a valid account in the system |
| Notes | Virtual coins and diamonds may be exchanged for any item in the store.|
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |


#### Play virtual prize party mode

| UC.7 | Play virtual prize party mode |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to play using virtual coins as a wager |
| Basic flow | 1. Log in|
|            | 2. Play virtual prize party mode|
| Pre-conditions | Log in |  
| Post-conditions  | Select table size|  
| Requirements | Have a valid account in the system |
| Notes | This is a paid game mode |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Play real prize party mode

| UC.8 | Play real prize party mode|
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to play using real money as a wager|
| Basic flow | 1. Log in|
|            | 2. Play real prize party mode|
| Pre-conditions | Log in |  
| Post-conditions  | Select table size|  
| Requirements | Have a valid account in the system|
| Notes | This is a paid game mode |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Play friends party mode

| UC.9 | Play friends party mode |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows to have a match between your friends |
| Basic flow | 1. Log in|
|            | 2. Play friends party mode|
| Pre-conditions |Log in |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | This is a free game mode |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Send and receive friend requests

| UC.9 | Send and receive friend requests |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to add friends within the app |
| Basic flow | 1. Log in|
|            | 2. Send and receive friend requests|
| Pre-conditions |Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system  |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Personalice skins

| UC.10 | Personalice skins |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to customize the appearance of the board, dice, avatars, etc. |
| Basic flow | 1. Log in|
|            | 2. Personalice skins|
| Pre-conditions | Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Search player

| UC.11 | Search player |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows the user to search another user |
| Basic flow | 1. Log in|
|            | 2. Search player|
| Pre-conditions | Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Receive friend request

| UC.12 | Receive friend request |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows the user to receive a friend request from other user |
| Basic flow | |
| Pre-conditions | Log in|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Advanced settings

| UC.13 | Advanced settings |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to configure different advanced settings, such as your username, password, modify your credit card, withdraw funds, etc. |
| Basic flow | 1. Log in|
|            | 2. Advanced settings|
| Pre-conditions | Log in |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Consult scoreboards

| UC.14 | Consult scoreboards |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to consult the leaderboards and high score rankings, globally and among your friends |
| Basic flow | 1. Log in|
|            | 2. Consult scoreboards|
| Pre-conditions | Login|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Buy diamonds

| UC.15 | Buy diamonds |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to buy diamonds to use it in the aplication|
| Basic flow | 1. Log in|
|            | 2. Shopping in the store|
|            | 3. Buy diamonds|
| Pre-conditions | Shopping in the store|  
| Post-conditions  | Check credit card |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Select table size

| UC.16 | Select table size |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to select the number of players user will be playing against|
| Basic flow(1) | 1. Log in|
|            | 2. Play virtual party mode|
|            | 3. Select table size|
| Basic flow(2) | 1. Log in|
|            | 2. Play real party mode|
|            | 3. Select table size|
| Pre-conditions | Play paid game mode(UC.7 or UC.8)|  
| Post-conditions  | Select stake level |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Select stake level

| UC.17 | Select stake level |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to select the stake level of user's game table|
| Basic flow(1) | 1. Log in|
|            | 2. Play virtual party mode|
|            | 3. Select table size|
|            | 4. Select stake level|
| Basic flow(2) | 1. Log in|
|            | 2. Play real party mode|
|            | 3. Select table size|
|            | 4. Select stake level|
| Pre-conditions | Select table size|  
| Post-conditions  | Check enough necessary token |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Check enough necessary token

| UC.18 | Check enough necessary token |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | |
| Description | Verify the amount of virtual coins and diamonds in the user account|
| Basic flow | |
| Pre-conditions | Select stake level|  
| Post-conditions  | |  
| Requirements | |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Check credit card 

| UC.19 | Check credit card |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Verify the status of the credit card |
| Basic flow | |
| Pre-conditions | Buy diamonds or deny operation(UC.15, UC.24) |  
| Post-conditions  | |  
| Requirements | |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Credit card exist

| UC.20 | Credit card exist |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | |
| Description | Verify that the credit card exists and is valid.|
| Basic flow ||
| Pre-conditions | Check credit card |  
| Post-conditions  | Return to main menu to be able to buy anything the user want|  
| Requirements | |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Credit card not exist

| UC.21 | Credit card not exist |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | |
| Description |Verify that the credit card doesn't exists or is not valid.|
| Basic flow | |
| Pre-conditions | Check credit card |  
| Post-conditions  | Add credit card |  
| Requirements |  |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Add credit card

| UC.22 | Add credit card |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description | Allows you to add your credit card to be able to play all modes |
| Basic flow(1) | 1. Log in |
|            | 2. Access paid game mode |
|            | 3. Select table size|
|            | 4. Select stake level |
|            | 5. Check enough necessary token|
|            | 6. Deny operation|
|            | 7. Check credit card |
|            | 8. Credit card not exist |
|            | 9. Add credit card |
| Basic flow(2) | 1. Log in |
|            | 2. Shopping in the store |
|            | 3. Check enough necessary token|
|            | 4. Deny operation|
|            | 5. Check credit card |
|            | 6. Credit card not exist |
|            | 7. Add credit card |
| Basic flow(3) | 1. Log in |
|            | 2. Shopping in the store |
|            | 3. Buy diamonds|
|            | 4. Check credit card |
|            | 5. Credit card not exist |
|            | 6. Add credit card |
| Pre-conditions | Credit card doesn't exist|  
| Post-conditions  | The user will return to the main menu to be able to play all modes and shop in the store|  
| Requirements | Have a bank account|
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Approve operation

| UC.23 | Approve operation |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | |
| Description | The system approve the desire operation because the user doesn't have enough virtual coins or diamonds|
| Basic flow ||
| Pre-conditions | Check enough necessary token|  
| Post-conditions  | |  
| Requirements | |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Deny operation

| UC.24 | Deny operation |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | |
| Description |The system deny the desire operation because the user doesn't have enough virtual coins or diamonds|
| Basic flow | |
| Pre-conditions | Check enough necessary token|  
| Post-conditions  | Check credit card|  
| Requirements |  |
| Notes | This use case is automatically done by the system |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Join game room

| UC.25 | Join game room |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to join a private game room with his friends|
| Basic flow |1. Log in |
|            |2. Play friends party mode |
|            |3. Join game room|
| Pre-conditions | Play friends party mode |  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Create game room

| UC.26 | Create game room |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to create a private game room to play with his friends|
| Basic flow |1. Log in |
|            |2. Play friends party mode |
|            |3. Create game room|
| Pre-conditions | Play friends party mode |
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Invite friends

| UC.27 | Invite friends |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to invite his friends to a specific game room|
| Basic flow |1. Log in |
|            |2. Play friends party mode |
|            |3. Create game room|
|            |4. Invite friends|
| Pre-conditions | Create game room|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Send friend request

| UC.28 | Send friend request |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to send a friend request to the searched player|
| Basic flow |1. Log in |
|            |2. Search player |
|            |3. Send friend request|
| Pre-conditions | Search player|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Consult player stats

| UC.29 | Consult player stats |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to view all the stats of the searched player (number of wins, losses, favorite tables... ) |
| Basic flow |1. Log in |
|            |2. Search player |
|            |3. Consult player stats|
| Pre-conditions | Search player|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Accept friend request

| UC.30 | Accept friend request |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to accept the friend request sent from other user|
| Basic flow |1. Log in |
|            |2. Receive friend request |
|            |3. Accept friend request |
| Pre-conditions | Receive friend request|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes | |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Decline friend request

| UC.31 | Decline friend request |
|---|---|
| Sources  | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | User |
| Description |Allows the user to decline the friend request sent from other user|
| Basic flow |1. Log in |
|            |2. Receive friend request |
|            |3. Decline friend request |
| Pre-conditions | Receive friend request|  
| Post-conditions  | |  
| Requirements | Have a valid account in the system |
| Notes |  |
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Send data

| UC.32 | Send data |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | Database |
| Description | Send necessary data for the different use cases of the system |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes | This UC is automatically done by the system|
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

#### Receive data

| UC.33 | Receive data |
|---|---|
| Sources | The use case is supported by [this document](https://github.com/samugd17/proyecto-ets/blob/develop/doc/use-case-diagram.md). |
| Actor | Database |
| Description | Receive necessary data for the different use cases of the system |
| Basic flow| |
| Pre-conditions | |  
| Post-conditions  | |  
| Requirements | |
| Notes | This UC is automatically done by the system|
| Autor  | _Samuel Eloy González Díaz & Jaime León_ |
| Date | _06/04/2023_ |

</div>
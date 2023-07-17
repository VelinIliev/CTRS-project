# Cinema Tickets Reservation System (CTRS)
<p>---- final project for Python Web Framework - SoftUni ----</p>

## <ins>Build with:<ins>
- Python
- Django
- PostgreSQL
- HTML
- Django template language
- CSS
- JavaScript
- Django Rest framework


## <ins>Description:</ins>
<p>CTRS is an automated movie ticket booking system designed to provide an easy-to-navigate and user-friendly experience.</p>

## <ins>Paths:</ins>
  
1. <b>Home Page (/)</b>:
    - <p>Landing page of the website.</p>
      <p><img src="./screenshots/index.png" alt="ctrs-index" width="600px"></p>

2. <b>Admin Section (admin/):</b>
   #### Fully configured admin section with the following groups:
   - Admins: Full control over the system. 
   - CinemaAdmin: CRUD operations for movies, halls, projections, and tickets. Can review users.
   - ContentCreator: Can create, edit, review movies and projections
   - Moderators: CRUD operations for movie comments.
   - UserAdmin: CRUD operations for users.
     <p><img src="./screenshots/admin.png" alt="ctrs-admin" width="600px">

3. <b>User Authentication and Registration (profile/):</b>
   - login/ - User login page.
   - logout/ - User logout page.
   - register/ - User registration page.
   - register/staff/ - Restricted to users with "add_user" permission. Allows registration as staff members.
   - details/<int:pk>/ - Only the owner can see the complete information and the reservations he has made.
   - delete/<int:pk>/ - Restricted to owner of profile.
   - edit/<int:pk>/ - Restricted to owner of profile.

4. <b>Movie Details and Management (movie/):</b>
   - index - Displays a list of all movies sorted by most recently added (paginated by 8). Includes a search field to search by title and an option to order by rating</p>
     <p><img src="./screenshots/movies-list.png" alt="ctrs-admin" width="600px"></p>
   - add/ - only users with this permission can add movie
   - details/<int:pk>/<str:slug>/ - Displays full information about a specific movie. Includes links to vote for the movie and view upcoming projections. Only logged-in users can comment.
     <p><img src="./screenshots/movie-details.png" alt="ctrs-admin" width="600px"></p>
   - edit/<int:pk>/<str:slug>/ - Restricted to users with "edit_movie" permission. Allows editing of movie details.
   - vote/<int:pk>/<str:slug>/ - Restricted to logged-in users. Allows users to vote for a movie (limited to one vote per movie).

5. <b>Hall Management (hall/): </b>
   - index - Displays a list of all halls.
   - add/ -  Restricted to users with "add_hall" permission. Allows adding a new hall.
   - details/<int:pk>/<str:slug>/ - Displays full information about a specific hall, including seating arrangement.
   - edit/<int:pk>/<str:slug>/ - Restricted to users with "edit_hall" permission. Allows editing of hall details.
   - delete/<int:pk>/<str:slug>/ -  Restricted to users with "delete_hall" permission. Allows deleting a hall.

6. <b>Projection Management (projection/): </b>
   - Displays a list of all projections for the next 7 days, starting from today. Ordered by movie and hour. Provides information about free seats for each projection.
     <p><img src="./screenshots/program.png" alt="ctrs-admin" width="600px"></p>
   - add/ - Restricted to users with "add_projection" permission. Allows adding a new projection.

7. <b>Ticket Management (ticket/) </b>
   - index - Displays a list of ticket types and prices.
   - add/ - Restricted to users with "add_ticket" permission. Allows adding a new ticket.
   - edit/<int:pk>/ - Restricted to users with "edit_ticket" permission. Allows editing of ticket details.
   - delete/<int:pk>/ - Restricted to users with "delete_ticket" permission. Allows deleting a ticket.

8. <b>Reservation (reservation/):</b>
   - start/ - Allows logged-in users to start a reservation for a selected movie, day, hour, and hall. Provides information about free seats in the hall.
     <p><img src="./screenshots/reservation-start.png" alt="ctrs" width="600px"></p>
   - step1/ - Allows users to select the number and type of tickets for their reservation.
     <p><img src="./screenshots/reservation-step1.png" alt="ctrs" width="600px"></p>
   - step2/ - Provides a seat selection interface for users to choose their seats in the hall.
     <p><img src="./screenshots/reservation-step2.png" alt="ctrs" width="600px"></p>
   - review/<int:pk>/ - Displays an overview of the reservation.

9. <b>API Integration (api/): </b> - 
   - Api integration for third party sites. Only GET requests.
   - movies/ - Retrieves a list of all movies. Supports search by title (?title=) and year (?year=).
   - movies/<int:movie_id>/ - Retrieves details of a single movie.
   - projections/ - Retrieves a list of all projections. Supports filtering by movie ID (?movie_id=), movie title (?movie_title=), start date (?start='dd-mm-yyyy'), and end date (?end='dd-mm-yyyy').
   - projections/<str:projection_date>/ - Retrieves a list of all projections on a specific date (format: 'dd-mm-yyyy').

<p><b><ins>Note: The administration links are visible only to staff users.</ins></b></p>
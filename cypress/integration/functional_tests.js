// **** end to end tests ****
describe('Visiting the main page', function () {
  it('Check that the title contains the site name', function () {
    // Visits the website running on localhost
    cy.visit('http://localhost:8000');
    // The user sees that the website is named Menrva Site
    cy.contains('Menrva Site');
    // the user clicks on the django link
    cy.contains('Soft Gripper').click();
    // The user creates a new topic
    cy.contains('New topic').click();
    // They fill in the form and post it
    cy.get('#id_subject').type('Adding a new subject');
    cy.get('#id_message').type('And the user adds a message to it');
    cy.contains('Post').click();
    // They are returned to the posts page
    cy.contains('Topic');
    cy.contains('Starter');

    // They see their post has been added to the list of posts
    cy.contains('Adding a new subject');
  });
});

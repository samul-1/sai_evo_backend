/*
 * Snippets API
 * Test description
 *
 * OpenAPI spec version: v1
 * Contact: contact@snippets.local
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.23
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SnippetsApi);
  }
}(this, function(expect, SnippetsApi) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('EventTemplate', function() {
      beforeEach(function() {
        instance = new SnippetsApi.EventTemplate();
      });

      it('should create an instance of EventTemplate', function() {
        // TODO: update the code to test EventTemplate
        expect(instance).to.be.a(SnippetsApi.EventTemplate);
      });

      it('should have the property name (base name: "name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property rules (base name: "rules")', function() {
        // TODO: update the code to test the property rules
        expect(instance).to.have.property('rules');
        // expect(instance.rules).to.be(expectedValueLiteral);
      });

    });
  });

}));
